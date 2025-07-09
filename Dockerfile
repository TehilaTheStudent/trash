# Use official Node.js LTS image
FROM node:20-slim

# Set working directory
WORKDIR /app

# Expose port (default for inspector is 3000, change if needed)
EXPOSE 6274

# Run inspector on container start
CMD ["sh", "-c", "HOST=0.0.0.0 npx -y @modelcontextprotocol/inspector"]
