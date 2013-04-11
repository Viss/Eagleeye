<?php

	$dir = ".";
	if(is_dir($dir)){
		if($dd = opendir($dir)){
			while (($f = readdir($dd)) !== false)
				if(preg_match("/.png/", $f)) {
					$files[] = $f;
				}
			closedir($dd);
		} 
	
	$response = "";
		foreach ($files as $img){
			echo $img.';';
		}
	}
?>
