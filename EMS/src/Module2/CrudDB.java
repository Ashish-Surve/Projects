package Module2;
import Module1.Employee;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class CrudDB {
	static Connection con;
	
	static 
    {
		try 
		{
			Class.forName("com.mysql.jdbc.Driver");  
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/Employee","root","");    
	    }
	    catch(Exception e)
	    { 
	    	System.out.println(e);
	    }  
 }


 public static void addEmp(Employee e) {
	 // connection1();
	 int i=-1;
		  try {
			  PreparedStatement pst=con.prepareStatement("INSERT INTO Employee (`name`, `salary`, `medical`) VALUES (? ,? ,?);");
			  pst.setString(1,e.getName());
			  pst.setDouble(2,e.getbSalary());
			  pst.setDouble(3,e.getMedical());
			  i=pst.executeUpdate();
		  }
		  catch(SQLException s)
		  {
			  s.printStackTrace();
			  System.out.println("DataBase Error Code: "+i);
			  
		  }
	  
	System.out.println("Record Inserted");
     
 }
public static void removeEmp(int aid) {
  
	int i=-1;
	try 
	{
		Statement st=con.createStatement();
		
		i=st.executeUpdate("delete from Employee where id="+aid);
	}
	catch(SQLException s)
	{
		s.printStackTrace();
		System.out.println("ERROR CODE: "+i);
	}
	
	//System.out.println("Record Deleted");
		  
}

public static void searchEmp() 
	{
	 // connection1();
		Scanner sc=new Scanner(System.in);
	 	int i=-1;
	 	int ch=0;
	 	String f="";
	 	String some="";
	 	System.out.println("Search by: \n1.ID\n2.Name\nSalary\n");
	 	ch=sc.nextInt();
		switch(ch)
		{
				
				case 1: System.out.println("Enter id?\n");
						some="id";
						f=sc.next();
						break;
				case 2: System.out.println("Enter Name?\n");
				 		some="name";
				 		f=sc.nextLine();
				 		break;
				case 3: System.out.println("Enter Salary?\n");
		 				some="salary";
		 				f=sc.nextLine();
		 				break; 		
		}			
		
	 
	  try 
	  {	  
		  	  
			  Statement st=con.createStatement();
			  //System.out.println(f+"\n"+some);
			  
			  ResultSet rs=st.executeQuery("Select * from Employee where "+some+" = "+f.trim());
			  System.out.println("\nName: "
				+"\tSalary: "
				+"\tid: "
				+"\tHRA: "
				+"\tPF: "
				+"\tPT: "
				+"\t Medical Allowance: "
				+"\tGross Salary: "
				+"\t Net Salary: ");
			  while(rs.next())
			  {
				  Employee e=new Employee(rs.getString(2),rs.getDouble(3),rs.getDouble(4));
				  System.out.print(e.toString());
			  }
			  
	  }
	  catch(SQLException s)
	  {
		  s.printStackTrace();
		  System.out.println("DataBase Error Code: "+i);
	  }
	  
    
}



}  
		   

