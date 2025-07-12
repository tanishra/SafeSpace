const Threat = require('../models/Threat');
const db = require('../services/firebase');

const threatController = {
  getThreats: async (req, res) => {
    try {
      const { severity, limit = 50 } = req.query;
      let query = db.collection('threats')
        .where('isActive', '==', true)
        .orderBy('timestamp', 'desc')
        .limit(parseInt(limit));

      if (severity) {
        query = query.where('severity', '==', severity);
      }

      const snapshot = await query.get();
      const threats = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }));

      res.json({
        success: true,
        data: threats,
        count: threats.length
      });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  },

  getNearbyThreats: async (req, res) => {
    try {
      const { lat, lng, radius = 5 } = req.query;

      if (!lat || !lng) {
        return res.status(400).json({ success: false, error: 'Latitude and longitude are required' });
      }

      const threats = await db.collection('threats')
        .where('isActive', '==', true)
        .get();

      const nearbyThreats = threats.docs
        .map(doc => ({ id: doc.id, ...doc.data() }))
        .filter(threat => {
          const distance = calculateDistance(
            parseFloat(lat),
            parseFloat(lng),
            threat.coordinates.lat,
            threat.coordinates.lng
          );
          return distance <= parseFloat(radius);
        });

      res.json({
        success: true,
        data: nearbyThreats,
        count: nearbyThreats.length
      });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  },

  createThreat: async (req, res) => {
    try {
      const threat = new Threat(req.body);
      const docRef = await db.collection('threats').add({
        ...threat,
        timestamp: new Date()
      });

      res.status(201).json({
        success: true,
        data: { id: docRef.id, ...threat }
      });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  },

  updateThreat: async (req, res) => {
    try {
      const { id } = req.params;
      await db.collection('threats').doc(id).update(req.body);
      res.json({ success: true, message: 'Threat updated successfully' });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  },

  deactivateThreat: async (req, res) => {
    try {
      const { id } = req.params;
      await db.collection('threats').doc(id).update({ isActive: false });
      res.json({ success: true, message: 'Threat deactivated successfully' });
    } catch (error) {
      res.status(500).json({ success: false, error: error.message });
    }
  }
};

// Simple Haversine formula for distance (km)
function calculateDistance(lat1, lon1, lat2, lon2) {
  const R = 6371;
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * Math.PI / 180) *
    Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

module.exports = threatController;
