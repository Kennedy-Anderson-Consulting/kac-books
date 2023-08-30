CREATE FUNCTION entry_balance_change(entry_id int, commodity varchar(5), value numeric) RETURNS void AS
$$
BEGIN
  LOOP
    BEGIN
      INSERT INTO temp_balance_changes (entry_id, commodity, value) VALUES (entry_id, commodity, value);
      EXIT;
    EXCEPTION
      WHEN undefined_table THEN
        CREATE TEMP TABLE temp_balance_changes (
          entry_id int,
          commodity varchar(5),
          value numeric
        );
    END;
  END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION split_row_insert_trigger_func() RETURNS trigger AS
$$
BEGIN
  PERFORM entry_balance_change(NEW.entry_id, NEW.commodity, NEW.value);
  RETURN NULL;
END;
$$ SECURITY DEFINER LANGUAGE plpgsql;

CREATE FUNCTION split_row_update_trigger_func() RETURNS trigger AS
$$
BEGIN
  PERFORM entry_balance_change(OLD.entry_id, OLD.commodity, -OLD.value);
  PERFORM entry_balance_change(NEW.entry_id, NEW.commodity, NEW.value);
  RETURN NULL;
END;
$$ SECURITY DEFINER LANGUAGE plpgsql;

CREATE FUNCTION split_row_delete_trigger_func() RETURNS trigger AS
$$
BEGIN
  PERFORM entry_balance_change(OLD.entry_id, OLD.commodity, -OLD.value);
  RETURN NULL;
END;
$$ SECURITY DEFINER LANGUAGE plpgsql;

CREATE FUNCTION assert_entry_changes_balance() RETURNS trigger AS
$$
BEGIN
  IF EXISTS(SELECT tablename FROM pg_tables WHERE tablename='temp_balance_changes') THEN
    IF 0 <> ANY (SELECT SUM(value) FROM temp_balance_changes GROUP BY entry_id, commodity) THEN
      RAISE;
    END IF;
    DROP TABLE temp_balance_changes;
  END IF;
  RETURN NULL;
END;
$$ SECURITY DEFINER LANGUAGE plpgsql;
