CREATE TRIGGER split_row_insert_trigger AFTER INSERT ON splits FOR EACH ROW EXECUTE FUNCTION split_row_insert_trigger_func();
CREATE TRIGGER split_row_update_trigger AFTER UPDATE ON splits FOR EACH ROW EXECUTE FUNCTION split_row_update_trigger_func();
CREATE TRIGGER split_row_delete_trigger AFTER DELETE ON splits FOR EACH ROW EXECUTE FUNCTION split_row_delete_trigger_func();

CREATE TRIGGER split_modify_statement_trigger AFTER INSERT OR UPDATE OR DELETE ON splits FOR EACH STATEMENT EXECUTE FUNCTION assert_entry_changes_balance();
