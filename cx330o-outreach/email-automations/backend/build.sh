#!/bin/bash

# Docker build optimization script for Cold Email Backend

set -e

echo "🐳 Docker Image Optimization Script"
echo "=================================="

# Function to show image size
show_size() {
    local image_name=$1
    echo "📊 Image size for $image_name:"
    docker images $image_name --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
}

# Function to build with different optimization levels
build_image() {
    local dockerfile=$1
    local tag=$2
    local context="."
    
    echo "🔨 Building $tag..."
    docker build -f $dockerfile -t $tag $context
    
    show_size $tag
}

# Clean up old images
echo "🧹 Cleaning up old images..."
docker system prune -f

# Build development image (original)
echo ""
echo "📦 Building development image..."
build_image "Dockerfile" "cold-email-backend:dev"

# Build production image (optimized)
echo ""
echo "🚀 Building production image..."
build_image "Dockerfile.prod" "cold-email-backend:prod"

# Compare sizes
echo ""
echo "📈 Size Comparison:"
echo "=================="
docker images cold-email-backend --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# Show detailed size breakdown
echo ""
echo "🔍 Detailed size breakdown for production image:"
docker history cold-email-backend:prod --format "table {{.CreatedBy}}\t{{.Size}}"

# Show final recommendations
echo ""
echo "✅ Build completed!"
echo ""
echo "💡 Usage:"
echo "  Development: docker run -p 8000:8000 cold-email-backend:dev"
echo "  Production:  docker run -p 8000:8000 cold-email-backend:prod"
echo ""
echo "🚀 For production deployment:"
echo "  docker-compose -f docker-compose.prod.yml up -d" 
