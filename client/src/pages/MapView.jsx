import React from "react";
import { MapPin } from "lucide-react";

const MapView = () => {
  return (
    <div className="bg-gray-800/30 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50 h-96">
      <h2 className="text-xl font-bold text-white mb-4 flex items-center">
        <MapPin className="w-6 h-6 mr-2 text-blue-400" />
        Threat Map
      </h2>
      <div className="bg-gray-700/30 rounded-lg h-80 flex items-center justify-center border border-gray-600/30">
        <div className="text-center">
          <MapPin className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <p className="text-gray-300">Interactive map will be integrated here</p>
          <p className="text-sm text-gray-400 mt-2">
            Shows real-time threat locations and safe routes
          </p>
        </div>
      </div>
    </div>
  );
};

export default MapView;
