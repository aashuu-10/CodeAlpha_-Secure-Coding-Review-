# Secure Coding Review Report

## Application

Python Login Authentication

## Review Tool

Bandit

## Findings

### 1. Hardcoded Credentials

**Issue:** Username and password are stored directly in the code.

**Recommendation:** Store credentials securely and use environment variables.

---

### 2. Plain Text Password

**Issue:** Password comparison is performed using plain text.

**Recommendation:** Use password hashing (bcrypt or Argon2).

---

### 3. Lack of Input Validation

**Issue:** User input is not validated.

**Recommendation:** Validate and sanitize user input before processing.

---

## Conclusion

The application works correctly but should follow secure coding practices to improve security.