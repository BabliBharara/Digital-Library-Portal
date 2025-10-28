<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
session_start();
// rest of your code...


// Database connection settings
$host = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "user_db";

// Create connection
$conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get data from form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Prepare SQL statement
    $sql = "SELECT id, password FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    
    if ($stmt) {
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        // Check if user exists
        if ($stmt->num_rows == 1) {
            $stmt->bind_result($id, $hashedPassword);
            $stmt->fetch();

            // Verify password
            if (password_verify($password, $hashedPassword)) {
                // Success - start session
                $_SESSION["user_id"] = $id;
                $_SESSION["username"] = $username;

                // Redirect to dashboard
                header("Location: dashboard.html"); // change if needed
                exit();
            } else {
                echo "❌ Incorrect password.";
            }
        } else {
            echo "❌ No account found with that username.";
        }

        $stmt->close();
    } else {
        echo "❌ Error in SQL preparation.";
    }
}

$conn->close();
?>

