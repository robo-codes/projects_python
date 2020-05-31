<%@ Page Language="C#" MasterPageFile="~/aMasterPage.master" AutoEventWireup="true" CodeFile="admin_login.aspx.cs" Inherits="admin_login" Title="Untitled Page" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
    <style type="text/css">
        .style1
        {
            width: 100%;
        }
        .style2
        {
            height: 18px;
        }
    </style>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <table class="style1">
        <tr>
            <td class="style2" colspan="2" align ="center" >
               <h2> Admin Login</h2></td>
        </tr>
        <tr>
            <td>
               UserName</td>
            <td>
            <asp:TextBox ID="username" runat="server"></asp:TextBox>
               </td>
        </tr>
        <tr>
            <td>
                Password</td>
            <td>
            <asp:TextBox ID="password" runat="server" TextMode="Password" Width="130px"></asp:TextBox>
                </td>
        </tr>
        <tr>
            <td colspan="2" align="center" >
                <asp:Button ID="login" Text="Login" runat="server" Width="65px"
                    onclick="login_Click" />

                </td>

        </tr>
    </table>
</asp:Content>
