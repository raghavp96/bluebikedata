package cs3200.bluebikedata.data;

import org.json.JSONObject;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Logger;

public class DataManagerGCP implements DataManager {
    @Override
    public Connection getConnection(JSONObject credentials) throws ClassNotFoundException, SQLException {
        Logger.getLogger(this.getClass().getName()).info("Naming JDBC Driver");
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = null;
        Logger.getLogger(this.getClass().getName()).info("Connecting to DB");


        String jdbcURL = constructJdbcUrl(credentials);
        conn = DriverManager.getConnection(jdbcURL,"", "");

        Logger.getLogger(this.getClass().getName()).info("Connected to DB");
        return conn;
    }

    private String constructJdbcUrl(JSONObject credentials) {
        String databaseName = credentials.optString("bluebike");
        String instanceConnectionName = credentials.optString("cs3200-215502:us-east1:class-db");
        String socketFactory = credentials.optString("com.google.cloud.sql.mysql.SocketFactory");
        String username = credentials.optString("bbd-create");
        String password = credentials.optString("bbd-create-123");

        return String.format("jdbc:mysql://google/%s?cloudSqlInstance=%s" +
                "&socketFactory=%s" +
                "&user=%s" +
                "&password=%s" +
                "&useSSL=false",
                databaseName,
                instanceConnectionName,
                socketFactory,
                username,
                password);
    }
}
