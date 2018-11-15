package cs3200.bluebikedata;

import cs3200.bluebikedata.data.DataManager;
import cs3200.bluebikedata.data.DataManagerGCP;
import org.json.JSONObject;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Logger;

import static spark.Spark.get;

public class Hello {

    private static Logger logger = Logger.getLogger("Hello");

    public static void main(String[] args) {
        get("/", (req, res) -> getSomething());
    }

    private static String getSomething() {
        DataManager manager = new DataManagerGCP();
        try {
            JSONObject credentials = new JSONObject();
            credentials.put("databaseName", "bluebike");
            credentials.put("instanceConnectionName ", "cs3200-215502:us-east1:class-db");
            credentials.put("socketFactory", "com.google.cloud.sql.mysql.SocketFactory");
            credentials.put("username", "bbd-create");
            credentials.put("password", "bbd-create-123");

            Connection connection = manager.getConnection(credentials);
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("select * from station");
            connection.close();
            JSONObject jsonObject = new JSONObject();

            while (resultSet.next()) {
                jsonObject.put("station_id", resultSet.getInt("station_id"));
                jsonObject.put("station_name", resultSet.getString("station_name"));
            }

            return jsonObject.toString(2);
        } catch (ClassNotFoundException | SQLException e) {
            logger.warning(e.getMessage());
            return e.getMessage();
        }

    }

}