<%@ Master Language="C#" AutoEventWireup="true" CodeFile="aMasterPage.master.cs" Inherits="aMasterPage" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <asp:ContentPlaceHolder id="head" runat="server">
    </asp:ContentPlaceHolder>
    <link href="template11/default.css" rel="stylesheet" type="text/css" />
    <link href="photo/template11/default.css" rel="stylesheet" type="text/css" />
</head>
<body>
    <form id="form1" runat="server">

   <div id="header">
	<div id="logo">
		<h1><a href="#"></a></h1>
		<h2><a href="http://www.freecsstemplates.org/">Express Ur Real Feelings</a></h2>
	</div>
	<div id="menu">
		<ul>

			<li class="first"><a href="aflowers_master_add.aspx">Flowers</a></li>
			<li><a href="acard_master_add .aspx">Card</a></li>
			<li><a href="acollectibles_master_add.aspx">Collectibles</a></li>
			<li><a href="agift_master_add.aspx">Gift</a></li>
			<li><a href="aspecial_master_add.aspx">Special</a></li>
			<li><a href="home.aspx">Logout</a></li>
		</ul>
	</div>
</div>
<!-- end header -->
<div id="page">
&nbsp;<!-- end sidebar --><asp:ContentPlaceHolder ID="ContentPlaceHolder1" runat="server">
        <p>
            <br />
        </p>
        <p>
        </p>
    </asp:ContentPlaceHolder>
</div>
<!-- end page -->

<div id="footer">
<br />
<br />
<h2><a href="home.aspx">Home</a> |
		    <a href="flower_list.aspx">Flower</a>|
			<a href="card_list.aspx">Card</a>|
			<a href="gift_list.aspx">Gift</a>|
			<a href="collectibles_list.aspx">Collectibles</a>|
			<a href="special_list.aspx">Special</a>|
			<a href ="home.aspx" >Logout</a>| </h2>
<p id="legal">&copy;2012 | Designed by <a href="http://www.freecsstemplates.org/">Bhoomika & Binita</a></p>
</div>




    </form>
</body>
</html>
