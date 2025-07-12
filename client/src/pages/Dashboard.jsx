import React from "react";
import { AlertTriangle, Shield, Brain, Zap, Eye } from "lucide-react";
import ThreatCard from "../components/ThreatCard";

const Dashboard = ({ threats }) => {
  return (
    
    <div className="space-y-8">
      <div className="text-center py-16">
        <h1 className="text-5xl font-bold text-white mb-4">
          AI-Powered Safety Intelligence
        </h1>
        <p className="text-xl text-gray-400 mb-8 max-w-2xl mx-auto">
          Real-time threat detection and analysis. Powered by advanced NLP and
          machine learning.
        </p>
        <div className="flex items-center justify-center space-x-4">
          <button className="bg-white text-black px-6 py-3 rounded-lg font-medium hover:bg-gray-200 transition-colors">
            View Live Threats
          </button>
          <button className="text-white border border-gray-700 px-6 py-3 rounded-lg font-medium hover:border-gray-600 transition-colors">
            Start Monitoring
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Active Threats</p>
              <p className="text-3xl font-bold text-white">{threats.length}</p>
            </div>
            <AlertTriangle className="w-8 h-8 text-red-400" />
          </div>
        </div>
        <div className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">Safety Score</p>
              <p className="text-3xl font-bold text-white">87%</p>
            </div>
            <Shield className="w-8 h-8 text-green-400" />
          </div>
        </div>
        <div className="bg-gray-800/50 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">AI Analyses</p>
              <p className="text-3xl font-bold text-white">1,247</p>
            </div>
            <Brain className="w-8 h-8 text-purple-400" />
          </div>
        </div>
      </div>

      <div className="flex items-center space-x-8 border-b border-gray-800">
        <button className="pb-4 text-white border-b-2 border-white">Featured</button>
        <button className="pb-4 text-gray-400 hover:text-white transition-colors">Real-time</button>
        <button className="pb-4 text-gray-400 hover:text-white transition-colors">Analysis</button>
        <button className="pb-4 text-gray-400 hover:text-white transition-colors">Alerts</button>
        <button className="pb-4 text-gray-400 hover:text-white transition-colors">Map View</button>
        <div className="flex-1"></div>
        <button className="pb-4 text-gray-400 hover:text-white transition-colors">
          Browse all threats →
        </button>
      </div>

      <div className="bg-gray-800/30 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-bold text-white flex items-center">
            <Zap className="w-6 h-6 mr-2 text-yellow-400" />
            Real-time Threat Detection
          </h2>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <span className="text-sm text-gray-400">Live</span>
          </div>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {threats.map((threat) => (
            <ThreatCard key={threat.id} threat={threat} />
          ))}
        </div>
      </div>

      <div className="bg-gray-800/30 backdrop-blur-sm rounded-xl p-6 border border-gray-700/50">
        <h3 className="text-lg font-semibold text-white mb-4 flex items-center">
          <Eye className="w-5 h-5 mr-2 text-blue-400" />
          AI Intelligence Dashboard
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-gray-700/30 rounded-lg p-4 border border-gray-600/30">
            <h4 className="font-medium text-white mb-2">Pattern Recognition</h4>
            <p className="text-sm text-gray-300">
              Detected unusual social media activity patterns in downtown area
            </p>
          </div>
          <div className="bg-gray-700/30 rounded-lg p-4 border border-gray-600/30">
            <h4 className="font-medium text-white mb-2">Sentiment Analysis</h4>
            <p className="text-sm text-gray-300">
              Overall public sentiment: 72% positive, trending downward
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
