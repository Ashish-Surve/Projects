package Module1;

import java.io.Serializable;

/**
 * Employee of a Company that has regular descriptions and unique ids.
 * @author Team OpenSource Evangelist
 *
 */
public strictfp class Employee implements Comparable<Employee>,Serializable {
	String name;
	//transient keyword is used when I don't want to save it to a file using serilizable.
	private double bSalary; // after reading salary=0;
	private double HRA;
	private double medical;
	private double pF;
	private double pT;
	private double netSalary;
	private double grossSalary;
	private int id;
	/**
	 * Empty Constructor only for object Creation. Initilized values are default.
	 */
	public Employee(){
		
		this("",0);
		
	}
	/**
	 * You are encouraged to use this as default.
	 * @param i id of the Employee
	 * @param n Name of the Employee
	 * @param sal Basic Salary of the Employee
	 */
	public Employee(String n,double sal)
	{
		name=n;
		bSalary=sal;
		HRA=0.5*bSalary;
		pF=0.12*bSalary;
		pT=200;
		medical=500;
		grossSalary=calculateGrossSalary();
		netSalary=calculateNetSalary();
	}
	/**
	 * Another Parameterized Constructor that uses Constructor chaining
	 * @param i id of the Employee
	 * @param n Name of the Employee
	 * @param sal Basic Salary of the Employee
	 * @param med Medical Allowance of the Employee
	 */
	public Employee(String n,double sal,double med)
	{
		this(n,sal);
		medical=med;
		
	}

	@Override
	public String toString()
	{
		return "\n"+name
				+"\t "+bSalary
				+"\t "+id
				+"\t "+HRA
				+"\t "+pF
				+"\t "+pT
				+"\t "+medical
				+"\t "+grossSalary
				+"\t "+netSalary+"\n\n";
	}
	/**
	 * Calculation of Gross Salary
	 * @return Gross Salary of the Employee
	 */
	private double calculateGrossSalary()
	{
		grossSalary=bSalary+HRA+medical+pT;
		return grossSalary;
		
	}
	/**
	 * Calculation of Net Salary
	 * @return Net Salary of the Employee
	 */
	private double calculateNetSalary()
	{
		netSalary=bSalary+HRA+medical+pF;
		return netSalary;
	}
	@Override
	public int hashCode()
	{
		return (int) (31*bSalary+31*medical+name.hashCode());
	}
	
	@Override
	public boolean equals(Object other)
	{
		if(this==other)
			return true;
		else if(other==null)
			return false;
		else if (!(other instanceof Employee))
            return false; 
		else
		{
			Employee m=(Employee)other;
			if(m.getbSalary()==this.getbSalary() 
				&& m.getName().equals(this.getName()) 
				&& this.getMedical()==m.getMedical())
			{
				return true;
			}
			
		}
		return false;
	}
/**
 * 
 * @return name of Employee
 */
	public String getName() {
		return name;
	}
	/**
	 * 
	 * @return Basic Salary
	 */
	public double getbSalary() {
		return bSalary;
	}
	/**
	 * 
	 * @param bSalary Basic Salary
	 */
	public void setbSalary(double bSalary) {
		this.bSalary = bSalary;
	}
	/**
	 * 
	 * @return Medical Allowance
	 */
	public double getMedical() {
		return medical;
	}
	/**
	 * 
	 * @param medical Medical Allowance
	 */
	public void setMedical(double medical) {
		this.medical = medical;
	}
	/**
	 * 
	 * @return id of Employee
	 */
	public int getId() {
		return id;
	}
	/**
	 * 
	 * @param id of Employee
	 */
	public void setId(int id) {
		this.id = id;
	}
	
	@Override
	public int compareTo(Employee arg0) {
		// TODO Auto-generated method stub
		if((arg0 instanceof Employee))
		{
			return (int) (this.bSalary-arg0.bSalary);
		}
		
		
		return -1;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee emp=new Employee("Saish",90000);
		Employee emp1=new Employee("Anand",80000,800);
		System.out.println(emp.toString());
		System.out.println(emp1.toString());
		char cc='1';
		
		int tem=Integer.parseInt(String.valueOf(cc).trim());
		System.out.println(tem==8);
		

	}


}