-- Створення користувача, якщо його ще не існує
DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'myuser') THEN
        CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';
    END IF;
END $$;

-- Створення бази даних, якщо її ще не існує
DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mydatabase') THEN
        CREATE DATABASE mydatabase;
    END IF;
END $$;
