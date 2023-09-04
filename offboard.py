import detach_and_delete_roles
import delete_policies
import delete_ips

def main():
    account_id = input("Enter your AWS account number: ")
   
    # Execute the functions from each script in the desired order
    detach_and_delete_roles.execute(account_id)
    delete_policies.execute(account_id)
    delete_ips.execute(account_id)

if __name__ == "__main__":
    main()

