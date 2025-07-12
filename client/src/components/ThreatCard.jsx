import React from "react";
import { AlertTriangle, MapPin } from "lucide-react";

const getSeverityColor = (severity) => {
  switch (severity) {
    case "high":
      return "from-red-500 to-red-600";
    case "medium":
      return "from-yellow-500 to-orange-500";
    case "low":
      return "from-green-500 to-green-600";
    default:
      return "from-gray-500 to-gray-600";
  }
};

const getSeverityBg = (severity) => {
  switch (severity) {
    case "high":
      return "bg-red-900/20 border-red-500/30 text-red-300";
    case "medium":
      return "bg-yellow-900/20 border-yellow-500/30 text-yellow-300";
    case "low":
      return "bg-green-900/20 border-green-500/30 text-green-300";
    default:
      return "bg-gray-900/20 border-gray-500/30 text-gray-300";
  }
};

const ThreatCard = ({ threat }) => {
  return (
    <div className="bg-gray-800/50 rounded-xl backdrop-blur-sm border border-gray-700/50 hover:border-gray-600/50 transition-all duration-300 overflow-hidden transform hover:scale-[1.02] hover:shadow-xl">
      <div className={`h-1 bg-gradient-to-r ${getSeverityColor(threat.severity)}`}></div>
      <div className="p-6">
        <div className="flex items-start justify-between mb-4">
          <div className="flex items-center space-x-3">
            <div className={`p-2 rounded-lg ${getSeverityBg(threat.severity)}`}>
              <AlertTriangle className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-semibold text-white">{threat.type}</h3>
              <p className="text-sm text-gray-400">{threat.time}</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <span className="text-sm font-medium text-gray-300">AI Confidence:</span>
            <span className="text-sm font-bold text-blue-400">{threat.confidence}%</span>
          </div>
        </div>
        <p className="text-gray-300 mb-4">{threat.description}</p>
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-1 text-gray-400">
              <MapPin className="w-4 h-4" />
              <span className="text-sm">{threat.location}</span>
            </div>
            <div className="flex items-center space-x-1 text-gray-400">
              <span className="text-sm">{threat.distance} away</span>
            </div>
          </div>
          <div className="text-xs text-gray-500 bg-gray-700/50 px-3 py-1 rounded-full">
            {threat.source}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ThreatCard;