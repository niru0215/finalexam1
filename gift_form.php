<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Selection</title>
</head>
<body>
    <h1>Gift Selection Extravaganza</h1>
    <form action="gift_selector.py" method="get">
        <label>Select Gifts:</label><br>
        <input type="checkbox" name="gifts" value="0"> Book<br>
        <input type="checkbox" name="gifts" value="1"> Toy<br>
        <input type="checkbox" name="gifts" value="2"> Gadget<br>
        <input type="checkbox" name="gifts" value="3"> Video Game<br>
        <!-- Add more gift options -->
        <input type="submit" value="Submit">
    </form>
</body>
</html>
