function createChild() {
	var parent = document.getElementById("parent");
	var table_column = document.createElement("tr");
	var table_row1 = document.createElement("th");
	var table_row2 = document.createElement("th");
	var input = document.createElement("input");
	var sibling = document.getElementById("add-btn")

	input.setAttribute("type", "text");
	input.setAttribute("name", "url");
	input.setAttribute("required", "");
	table_column.setAttribute("class", "url_row");
    
	table_row2.appendChild(input);
	table_column.appendChild(table_row1);
	table_column.appendChild(table_row2);
	parent.insertBefore(table_column, sibling);
}