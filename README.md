# Assessment

## To run the code
1. Clone this repository.
```bash
git clone https://github.com/pushkya/Assessment.git
```

2. Change directory to cloned repository.
```bash
cd Assessment
```

3. Install dependencies.
```bash
make pip-install
```

4. Run `make` command to configure aws shell.
```bash
make aws-configure
```

5. Pull and start docker containers.
```bash
make start
```

6. Run Python code to perform ETL process.
```bash
make perform-etl
```

##Postgres 
- To check if messages are loaded correctly on postgres
```bash
psql -d postgres -U postgres -p 5432 -h localhost -W
```
- Credentials and database information
    - **username**=`postgres`
    - **password**=`postgres`
    - **database**=`postgres`

- If `psql` binary is not installed use below command.
```bash
apt install postgresql-client
```

## Recovering masked PII
- The `ip` and `device_id` fields are masked using base64 encoding. Use the below command to decode
```bash
echo -n "<sample_base64_encrypted_string>" | base64 --decrypt
```
## Output video


https://user-images.githubusercontent.com/47081733/213054346-0842a4ec-799a-4494-8ff5-e67c69fb9557.mp4

