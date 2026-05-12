# 🛠️ FinShield Setup Guide

This guide provides comprehensive instructions for setting up the FinShield AML Detection Platform.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Variables](#environment-variables)
3. [Database Setup](#database-setup)
4. [Redis Setup](#redis-setup)
5. [API Keys](#api-keys)
6. [Installation](#installation)
7. [Running the Application](#running-the-application)
8. [Verification](#verification)
9. [Troubleshooting](#troubleshooting)

---

## 🔧 Prerequisites

### Required Software

| Software | Version | Purpose |
|----------|---------|---------|
| Python | 3.11+ | Runtime environment |
| PostgreSQL | 15+ | Primary database |
| Redis | 7+ | Caching layer |
| Docker | 24+ | Containerization (optional) |
| Docker Compose | 2.0+ | Multi-container orchestration (optional) |

### System Requirements

- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: Minimum 10GB free space
- **CPU**: 2+ cores recommended
- **Network**: Internet access for API calls

---

## 🔐 Environment Variables

Create a `.env` file in the project root with the following variables:

### Required Variables

```bash
# ======================
# REQUIRED CONFIGURATION
# ======================

# Groq API Key (Get from https://console.groq.com/)
GROQ_API_KEY=your_groq_api_key_here

# PostgreSQL Database Connection
DATABASE_URL=postgresql+asyncpg://finshield:your_secure_password@localhost:5432/finshield

# Redis Connection
REDIS_URL=redis://localhost:6379/0
```

### Optional Variables

```bash
# ======================
# OPTIONAL CONFIGURATION
# ======================

# API Server Settings
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4
API_RELOAD=false

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# Security
SECRET_KEY=your_super_secret_key_change_in_production
API_KEY_HEADER=X-API-Key
CORS_ORIGINS=["http://localhost:3000"]

# Risk Thresholds
RISK_THRESHOLD_LOW=30
RISK_THRESHOLD_MEDIUM=50
RISK_THRESHOLD_HIGH=70
RISK_THRESHOLD_CRITICAL=85

# LLM Configuration
LLM_MODEL=llama3-70b-8192
LLM_TEMPERATURE=0.1
LLM_MAX_TOKENS=4096

# Caching
ENABLE_CACHE=true
CACHE_TTL=3600

# Feature Flags
ENABLE_CRYPTO_ANALYSIS=true
ENABLE_PEP_SCREENING=true
ENABLE_SANCTIONS_SCREENING=true
ENABLE_NETWORK_ANALYSIS=true

# Monitoring
ENABLE_METRICS=true
METRICS_PORT=9090
```

---

## 🗄️ Database Setup

### Option 1: Docker PostgreSQL (Recommended for Development)

```bash
# Pull and run PostgreSQL container
docker run -d \
  --name finshield-postgres \
  -e POSTGRES_USER=finshield \
  -e POSTGRES_PASSWORD=your_secure_password \
  -e POSTGRES_DB=finshield \
  -p 5432:5432 \
  -v finshield-postgres-data:/var/lib/postgresql/data \
  postgres:15-alpine

# Verify connection
docker exec -it finshield-postgres psql -U finshield -d finshield -c "\dt"
```

### Option 2: Local PostgreSQL Installation

#### Windows

1. Download PostgreSQL from https://www.postgresql.org/download/windows/
2. Run the installer and follow the wizard
3. Remember the password you set for the `postgres` user
4. Open pgAdmin or psql and create the database:

```sql
-- Connect as postgres user first
CREATE USER finshield WITH PASSWORD 'your_secure_password';
CREATE DATABASE finshield OWNER finshield;
GRANT ALL PRIVILEGES ON DATABASE finshield TO finshield;

-- Connect to finshield database and enable UUID extension
\c finshield
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

#### Linux (Ubuntu/Debian)

```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create user and database
sudo -u postgres psql << EOF
CREATE USER finshield WITH PASSWORD 'your_secure_password';
CREATE DATABASE finshield OWNER finshield;
GRANT ALL PRIVILEGES ON DATABASE finshield TO finshield;
\c finshield
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOF
```

#### macOS

```bash
# Using Homebrew
brew install postgresql@15
brew services start postgresql@15

# Create user and database
psql postgres << EOF
CREATE USER finshield WITH PASSWORD 'your_secure_password';
CREATE DATABASE finshield OWNER finshield;
GRANT ALL PRIVILEGES ON DATABASE finshield TO finshield;
\c finshield
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOF
```

### Initialize Database Schema

After setting up PostgreSQL, run migrations:

```bash
# Using Alembic
alembic upgrade head

# Or using the CLI
finshield init-db
```

---

## 📦 Redis Setup

### Option 1: Docker Redis (Recommended)

```bash
# Pull and run Redis container
docker run -d \
  --name finshield-redis \
  -p 6379:6379 \
  -v finshield-redis-data:/data \
  redis:7-alpine redis-server --appendonly yes

# Verify connection
docker exec -it finshield-redis redis-cli ping
# Should return: PONG
```

### Option 2: Local Redis Installation

#### Windows

1. Download Redis from https://github.com/microsoftarchive/redis/releases
2. Or use Windows Subsystem for Linux (WSL2) with Ubuntu

```bash
# In WSL2 Ubuntu
sudo apt update
sudo apt install redis-server
sudo service redis-server start
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Verify
redis-cli ping
```

#### macOS

```bash
brew install redis
brew services start redis

# Verify
redis-cli ping
```

---

## 🔑 API Keys

### Groq API Key (Required)

1. Go to https://console.groq.com/
2. Sign up or log in
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy the key and add to your `.env` file:

```bash
GROQ_API_KEY=gsk_your_api_key_here
```

**Note**: Groq offers a generous free tier perfect for development and testing.

---

## 📥 Installation

### Using pip (Development)

```bash
# Clone the repository
git clone https://github.com/KUNALSHAWW/SentinelAI-AML.git
cd FinShield-AML

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment template
copy .env.example .env  # Windows
cp .env.example .env    # Linux/macOS

# Edit .env with your configuration
```

### Using Docker Compose (Recommended for Production)

```bash
# Clone the repository
git clone https://github.com/KUNALSHAWW/SentinelAI-AML.git
cd FinShield-AML

# Copy environment template
copy .env.example .env  # Windows
cp .env.example .env    # Linux/macOS

# Edit .env with your GROQ_API_KEY

# Build and start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

---

## 🚀 Running the Application

### Development Mode

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Start the server with auto-reload
finshield serve --reload

# Or using uvicorn directly
uvicorn finshield.api.app:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
# Using the CLI
finshield serve --workers 4

# Or using Docker Compose
docker-compose up -d
```

### Using Makefile

```bash
# Development
make dev

# Production
make run

# With Docker
make docker-up
```

---

## ✅ Verification

### 1. Check API Health

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "database": "connected",
  "redis": "connected",
  "llm": "ready"
}
```

### 2. Access API Documentation

Open in your browser:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 3. Test Analysis Endpoint

```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "transaction": {
      "amount": 50000,
      "currency": "USD",
      "transaction_type": "WIRE_TRANSFER",
      "origin_country": "US",
      "destination_country": "CA"
    },
    "customer": {
      "name": "Test Company Inc",
      "customer_type": "CORPORATE",
      "account_age_days": 365
    }
  }'
```

### 4. Check Metrics (if enabled)

```bash
curl http://localhost:8000/metrics
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Connection Error

```
Error: Could not connect to PostgreSQL
```

**Solutions:**
- Verify PostgreSQL is running: `docker ps` or `sudo systemctl status postgresql`
- Check DATABASE_URL in .env
- Ensure password has no special characters that need escaping
- Try connecting manually: `psql -h localhost -U finshield -d finshield`

#### 2. Redis Connection Error

```
Error: Could not connect to Redis
```

**Solutions:**
- Verify Redis is running: `docker ps` or `redis-cli ping`
- Check REDIS_URL in .env
- Default port is 6379

#### 3. Groq API Error

```
Error: Invalid API Key
```

**Solutions:**
- Verify GROQ_API_KEY is set correctly in .env
- Check for leading/trailing whitespace
- Regenerate API key if needed
- Check Groq console for rate limits

#### 4. Port Already in Use

```
Error: Address already in use
```

**Solutions:**
- Find process: `netstat -ano | findstr :8000` (Windows)
- Kill process: `taskkill /PID <pid> /F` (Windows)
- Or change API_PORT in .env

#### 5. Import Errors

```
Error: ModuleNotFoundError
```

**Solutions:**
- Ensure virtual environment is activated
- Run `pip install -e ".[dev]"`
- Check Python version: `python --version` (need 3.11+)

### Getting Help

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/KUNALSHAWW/SentinelAI-AML/issues)
2. Search for similar problems
3. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Environment details (OS, Python version, etc.)

---

## 📊 Quick Reference

### Environment Variables Summary

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GROQ_API_KEY` | ✅ | - | Groq API key |
| `DATABASE_URL` | ✅ | - | PostgreSQL connection string |
| `REDIS_URL` | ❌ | `redis://localhost:6379` | Redis connection |
| `API_HOST` | ❌ | `0.0.0.0` | API bind host |
| `API_PORT` | ❌ | `8000` | API port |
| `LOG_LEVEL` | ❌ | `INFO` | Logging level |
| `ENABLE_CACHE` | ❌ | `true` | Enable Redis caching |

### Service Ports

| Service | Default Port | Purpose |
|---------|-------------|---------|
| FinShield API | 8000 | REST API |
| PostgreSQL | 5432 | Database |
| Redis | 6379 | Cache |
| Prometheus | 9090 | Metrics |
| Grafana | 3000 | Dashboards |

---

**🎉 You're all set! Start analyzing transactions with FinShield.**
