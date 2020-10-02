<?php include('server.php'); ?>
<!DOCTYPE html>
    <head>
    <meta charset="UTF-8">
    <title>Insert and Retrieve data from MySQL database</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="scripts.js"></script>
    </head>
    <body>
    <div class="wrapper">
        <?php echo $comments; ?>
        <form class="comment_form">
        <div>
            <label for="name">Name:</label>
            <input type="text" name="name" id="name">
        </div>
        <div>
            <label for="comment">Comment:</label>
            <textarea name="comment" id="comment" cols="30" rows="5"></textarea>
        </div>
        <button type="button" id="submit_btn">POST</button>
        <button type="button" id="update_btn" style="display: none;">UPDATE</button>
        </form>
    </div>
    </body>
    
</html>
    