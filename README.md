# unittest_nextman


This project contains automated test scripts for the `nextman` tool, using Python's `unittest` framework. The scripts cover both backend and user-related functionalities.
1. **Environment Setup**  

2. **Run Tests**  
   In your terminal, navigate to the `unittest_nextman` folder and run:
   ```
   python unittestBACKEND.py
   python unittestUSER.py
   ```

3. **Notes**  
   - The tests invoke `nextman` commands via subprocess.  
   - Some tests will create, update, or delete LDAP users.  
   - Output is printed to the terminal for inspection.  
   - Assertions are used to check command results.
