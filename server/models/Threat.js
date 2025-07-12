class Threat {
  constructor(data) {
    this.type = data.type;
    this.location = data.location;
    this.coordinates = {
      lat: data.coordinates?.lat || 0,
      lng: data.coordinates?.lng || 0,
    };
    this.severity = data.severity || 'low';
    this.confidence = data.confidence || 50;
    this.description = data.description || '';
    this.source = data.source || 'user';
    this.timestamp = data.timestamp || new Date();
    this.isActive = data.isActive !== undefined ? data.isActive : true;
    this.aiAnalysis = data.aiAnalysis || {
      keywords: [],
      sentiment: 0,
      rawData: {},
    };
  }
}

module.exports = Threat;

