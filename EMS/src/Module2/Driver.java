package Module2;
import Module1.Employee;

import java.util.Scanner;

public class Driver {
    public void login() {
    	int id;
    	String pass;
    	 Scanner sc=new Scanner(System.in);
    	System.out.println("Enter id");
    	id=sc.nextInt();
    	System.out.println("Enter password");
    	pass=sc.next();
    	
      }
	
  public static void main(String[] args) {
		// TODO Auto-generated method stub
      System.out.println("Enter your choice:\n 1.admin \n 2.Employee ");
      int ch;
      Scanner sc=new Scanner(System.in);
      ch=sc.nextInt();
      Driver m1=new Driver();
      switch(ch) {
      	case 1:	
    	  		System.out.println("Enter your choice \n 1.Add Employee\n 2.Remove Employee \n 3.Search Employee");
    	  		int ch1;
    	  		ch1=sc.nextInt();
    	  			switch(ch1) 
    	  			{
    	  				case 1:
    	  						String name;
    	  						double salary, medical;
    	  						System.out.println("Enter Employee Name: ");
    	  						sc.nextLine();
    	  						name= sc.nextLine();
    	  						System.out.println("Enter Employee Salary: ");
    	  						salary = sc.nextDouble();
    	  						System.out.println("Enter Employee medical: ");
    	  						medical = sc.nextDouble();
    	  						CrudDB.addEmp(new Employee(name,salary,medical));
    	  						//insert into db
    	  						
    	  						break;
    	  				case 2: System.out.println("Enter id to remove?");
    	  						int f=sc.nextInt();
    	  					 	CrudDB.removeEmp(f);
    	  					 	System.out.println("Record Deleted");
    	  					//remove
    	  						break;
    	  				case 3: CrudDB.searchEmp();
    	  						break;
    	  						
    	  				default:
    	  						System.out.println("Enter valid choice");
    	  			}
    	  break;
     
      	case 2: m1.login();
      			System.out.println("Enter your choice \n1.View Profile \n2.Edit");
      			int ch2;
      			ch2=sc.nextInt();
      			switch(ch2) 
      			{
      				case 1:
      						CrudDB.searchEmp();
      						break;
      					//display details
          
			        case 2:
				        	 //allow editing
			        		break;
				    default:
				        	System.out.println("Enter valid choice");
				}
				  break;
				    	  
				  default:
					  System.out.println("Enter valid choice");
       }
	}

}
