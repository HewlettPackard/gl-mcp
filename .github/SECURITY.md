# Security Policy

## Reporting Security Vulnerabilities

**Please do not report security vulnerabilities through public GitHub issues.**

### How to Report

**Email**: gl-mcp@hpe.com  
**Subject**: `[SECURITY] GL-MCP Vulnerability Report`

### What to Include

When reporting a security vulnerability, please include:

- **Description** of the vulnerability
- **Steps to reproduce** the issue  
- **Affected versions** (if known)
- **Potential impact** assessment
- **Suggested fixes** (if any)

### Response Process

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 5 business days  
- **Status Updates**: Weekly until resolution
- **Resolution**: We aim to address critical issues within 90 days

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Security Best Practices

### For Users

- Keep your HPE GreenLake credentials secure
- Use environment variables for sensitive configuration  
- Regularly update to the latest version
- Follow principle of least privilege

### For Contributors

- Never commit credentials or API keys
- Use secure coding practices
- Report security issues privately
- Follow our contribution guidelines

## Security Features

GL-MCP includes the following security features:

- **TLS encryption** for all API communications
- **OAuth2 authentication** with automatic token management
- **Input validation** on all API endpoints
- **Secure credential handling** via environment variables
- **Audit logging** for security events

---

*This security policy may be updated as the project evolves. Check back periodically for changes.*
