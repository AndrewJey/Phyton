<!DOCTYPE html>
<html>
<head lang="es">
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="http://localhost/Bottle/CSS/bootstrap.css"/>
    <script src="http://localhost/Bottle/JS/jquery-2.1.4.js"></script>
    <script src="http://localhost/Bottle/JS/index.js"></script>
    <title></title>
</head>
<body>
    <h1>Delete Product</h1>
    <br/>
    <form action="/products/delete" method="post">
        Id: <input type="text" name="id" id="id" readonly value="{{!id}}"/>

        <br/>
        <input value="Delete" type="submit" />
    </form>

</body>
<script type="text/javascript">getProducts();</script>
</html>