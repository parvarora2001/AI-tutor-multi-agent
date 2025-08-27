# Tutor Agent - Docker Setup

This setup allows you to run the Tutor Agent in a Docker container, which provides better memory management and allows the use of larger, more capable AI models.

## Prerequisites

- Docker installed on your system
- Docker Compose installed
- At least 4GB of available RAM

## Quick Start

1. **Run the application:**
   ```bash
   chmod +x run_docker.sh
   ./run_docker.sh
   ```

   Or manually:
   ```bash
   docker-compose up --build
   ```

2. **The application will:**
   - Build the Docker image with all dependencies
   - Download and cache AI models (first run may take 5-10 minutes)
   - Start the interactive tutoring session

## Benefits of Docker Setup

- **Better Memory Management**: Docker provides isolated memory allocation
- **Larger Models**: Can use `flan-t5-base` instead of `flan-t5-small`
- **Consistent Environment**: Same behavior across different systems
- **Model Caching**: Models are cached and reused between runs
- **Resource Control**: Memory limits prevent system crashes

## Directory Structure

```
Tutor Agent/
├── cache/           # Model cache (persisted)
├── results/         # Session results (persisted)
├── Dockerfile       # Container definition
├── docker-compose.yml # Orchestration
└── run_docker.sh    # Easy run script
```

## Configuration

### Memory Allocation
The Docker container is configured with:
- **Memory Limit**: 4GB
- **Memory Reservation**: 2GB

You can adjust these in `docker-compose.yml` if needed.

### Model Selection
The Docker setup uses `google/flan-t5-base` for better response quality.

## Troubleshooting

### Out of Memory
If you get memory errors:
1. Increase memory limit in `docker-compose.yml`
2. Close other applications to free RAM
3. Consider using a smaller model

### Slow Model Loading
- First run downloads models (~1GB)
- Subsequent runs use cached models
- Models are stored in `./cache` directory

### Interactive Input Issues
The container is configured for interactive input. If you have issues:
```bash
docker-compose run --rm tutor-agent python main.py
```

## Stopping the Application

- Press `Ctrl+C` to stop the container
- Or run: `docker-compose down`

## Clean Up

To remove all Docker artifacts:
```bash
docker-compose down --rmi all --volumes
rm -rf cache results
```
