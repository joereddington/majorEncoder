<html>
<head>
<title>Major Analysis Number Encoder</title>
</head>
<body>
<H1>Tool for finding keywords for major analysis</h1>
	This tool uses the numbering system shown by Derren Brown in the
	excellent book <a href="http://www.amazon.co.uk/Tricks-Mind-Derren-Brown/dp/1905026269">Trick of the mind</a>. For a (much better) tool that uses the older numbering system see <a href="http://www.rememberg.com/">http://www.rememberg.com/</a><br>
	<h1>Major Analysis Number Encoder</h1>
	<form action="majorEncoder.php" method="post">
		<label for="firstname">Number to encode (at least three digits
			please):</label> <input type="text" id="targetNumber"
			name="targetNumber" /><br /> <input type="submit"
			value="Generate results" name="submit" />
	</form>
<?php
if ($_POST != null) {
	
	$target = $_POST ['targetNumber'];
	if (strlen ( $target ) >= 3) {
		$f = '[waeiouyc]?';
		$regex = '/^' . $f . $target;
		echo 'You entered the target' . $target . '<br><br>';
		$regex = str_replace ( '1', 'l' . $f, $regex );
		$regex = str_replace ( '2', 'n' . $f, $regex );
		$regex = str_replace ( '3', 'm' . $f, $regex );
		$regex = str_replace ( '4', 'r' . $f, $regex );
		$regex = str_replace ( '5', '[fv]' . $f, $regex );
		$regex = str_replace ( '6', '[bp]' . $f, $regex );
		$regex = str_replace ( '7', 't' . $f, $regex );
		$regex = str_replace ( '8', '[sc]h' . $f, $regex );
		$regex = str_replace ( '9', '[gd]' . $f, $regex );
		$regex = str_replace ( '0', '[sz]' . $f, $regex );
		$lines = file ( 'words.txt' );
		
		$fl_array = preg_grep ( $regex . '$/', $lines );
		if (sizeof ( $fl_array ) > 0) {
			echo 'Exact matches: <br>';
			foreach ( $fl_array as $element ) {
				echo $element . '<br>';
			}
			echo '<br>';
		}
		$fl_array = preg_grep ( $regex . '/', $lines );
		if (sizeof ( $fl_array ) > 0) {
			echo 'Matches that allow  trailing characters: <br>';
			foreach ( $fl_array as $element ) {
				echo $element . '<br>';
			}
		} else {
			echo "No matches found for the input $target";
		}
	} else {
		echo 'Please enter at least three digits<br>';
	}
}
?>
</body>
</html>
