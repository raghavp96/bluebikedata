package cs3200.bluebikedata.data;

import org.json.JSONObject;

import java.sql.Connection;
import java.sql.SQLException;

public interface DataManager {
    Connection getConnection(JSONObject credentials) throws ClassNotFoundException, SQLException;
}
