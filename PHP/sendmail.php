<?php
// Vérifiez si le formulaire a été soumis
if (isset($_POST['newsteller']) && !empty($_POST['email'])) {
    // Récupérez l'email depuis le formulaire et validez-le
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    // Vérifiez si l'email est valide
    if ($email === false) {
        echo "L'email entré n'est pas valide.";
    } else {
        try {
            // Paramètres de connexion à la base de données
            $host = 'localhost';
            $dbname = 'groovebar';
            $username = 'root';
            $password = '   ';

            // Créez une nouvelle instance PDO et établissez une connexion
            $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);

            // Définir le mode d'erreur PDO sur Exception
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Requête SQL préparée pour éviter les injections SQL
            $stmt = $pdo->prepare("INSERT INTO newsteller (mail) VALUES (:mail)");

            // Liez le paramètre :mail à la variable $email
            $stmt->bindParam(':mail', $email, PDO::PARAM_STR);

            // Exécutez la requête préparée
            $stmt->execute();

            echo "L'email a été ajouté avec succès à la newsletter.";
        } catch(PDOException $e) {
            // S'il y a une erreur, la capturer et afficher le message
            die("Erreur de connexion à la base de données : " . $e->getMessage());
        }
    }
} else {
    echo "Aucun email soumis.";
    header('Location: ../index.html');
}
?>
