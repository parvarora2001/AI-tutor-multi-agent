#!/bin/bash

# Create necessary directories
mkdir -p cache results

echo "🐳 Building and running Tutor Agent in Docker..."
echo "📝 This will use a larger model for better responses"
echo "💾 Models will be cached in ./cache directory"
echo "📊 Results will be saved in ./results directory"
echo ""

# Build and run with docker-compose
docker-compose up --build

echo ""
echo "✅ Docker container stopped"
