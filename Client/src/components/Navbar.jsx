import React from "react";
import { Shield, Bell, Users, Search, Github } from "lucide-react";
import { NavLink } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="bg-black backdrop-blur-sm border-b border-black">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-8">
            <div className="flex items-center space-x-3">
              <div className="bg-white p-2 rounded-lg">
                <Shield className="w-6 h-6 text-black" />
              </div>
              <h1 className="text-xl font-bold text-white">SafeSpace</h1>
            </div>

            <nav className="hidden md:flex space-x-8">
              <NavLink to="/" className={({ isActive }) => isActive ? "text-white" : "text-gray-400 hover:text-white"}>Dashboard</NavLink>
              <NavLink to="/map" className={({ isActive }) => isActive ? "text-white" : "text-gray-400 hover:text-white"}>Map</NavLink>
            </nav>
          </div>

          <div className="flex items-center space-x-4">
            <div className="relative hidden md:block">
              <Search className="w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
              <input
                type="text"
                placeholder="Search threats..."
                className="bg-gray-800/50 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-sm text-white placeholder-gray-400 focus:outline-none focus:border-gray-600"
              />
              <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-xs text-gray-500">
                Ctrl K
              </div>
            </div>

            <button className="p-2 text-gray-400 hover:text-white transition-colors">
              <Github className="w-5 h-5" />
            </button>

            <button className="p-2 text-gray-400 hover:text-white transition-colors">
              <Bell className="w-5 h-5" />
            </button>

            <div className="w-8 h-8 bg-gray-700 rounded-full flex items-center justify-center">
              <Users className="w-4 h-4 text-gray-300" />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
