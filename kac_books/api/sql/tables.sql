CREATE TABLE commodities (
	symbol varchar(5) PRIMARY KEY,
	name text NOT NULL,
	description text,
	priced_in varchar(5) REFERENCES commodities NOT NULL
);

CREATE TABLE prices (
	price_id SERIAL PRIMARY KEY,
	commodity varchar(5) REFERENCES commodities NOT NULL,
	price_time timestamp NOT NULL,
	value numeric NOT NULL
);

CREATE TABLE accounts (
	name text PRIMARY KEY,
	code text,
	description text,
	category account_category NOT NULL,
	commodity varchar(5) REFERENCES commodities NOT NULL,
	parent text REFERENCES accounts,
	placeholder boolean NOT NULL DEFAULT FALSE
);

CREATE TABLE journal_entries (
	entry_id SERIAL PRIMARY KEY,
	transaction_date date NOT NULL,
	description text
);

CREATE TABLE splits (
	split_id SERIAL PRIMARY KEY,
	entry_id int REFERENCES journal_entries NOT NULL,
	memo text,
	account text REFERENCES accounts NOT NULL
	value numeric NOT NULL,
	commodity varchar(5) REFERENCES commodities NOT NULL
);
