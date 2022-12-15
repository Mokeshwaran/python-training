from exceptions import UserException
from typing import Optional, Any, Dict


class Company:
    """
    This class contains the getter, setter and deleter of companies.
    """
    company = {}
    c_id = 0

    def __init__(self, name: Optional[str] = 'c_name',
                 address: Optional[str] = 'c_address') -> None:
        self.name = name
        self.address = address

    def set_company(self, name: Optional[str] = 'c_name',
                    address: Optional[str] = 'c_address') -> None:
        """
        This method will create a new company by user given name and address.

        :param name: str given by the user
        :param address: str given by the user
        :return: None
        """
        self.c_id += 1
        self.company.__setitem__(self.c_id, [name, address])

    def get_company(self, c_id: Optional[int] = 0) -> Any:
        """
        This method will get a single company based on the company_id
        given by the user.

        :param c_id: int given by the user
        :return: List of company details
        """
        if self.company.get(c_id) is None:
            raise UserException("Cannot get company")
        return self.company[c_id]

    def get_companies(self) -> Dict:
        """
        This method will get all the companies from the dictionary.

        :return: Dict containing all companies
        """
        if len(self.company) == 0:
            return {"No data": "found"}
        return self.company

    def delete_company(self, c_id: Optional[int] = 0) -> Any:
        """
        This method will delete a certain company based on the company_id
        given by the user.

        :param c_id: int given by the user.
        :return: str when deleted successfully / delete failed
        """
        if self.company.get(c_id) is None:
            raise UserException("Cannot delete company")
        self.company.pop(c_id)


company = Company()
flag = True
while flag:
    choice = input("1. Add Company\n"
                   "2. View Company\n"
                   "3. View All Companies\n"
                   "4. Delete Company\n"
                   "Enter your choice: ")
    match choice:
        case '1':
            company_name = input("Enter company's name: ")
            company_address = input("Enter company's address: ")
            company.set_company(company_name, company_address)
            print("Company Added")

        case '2':
            company_id = input("Enter company's ID: ")
            try:
                get_company = company.get_company(int(company_id))
            except UserException:
                print("Cannot get data")
            else:
                print(get_company)

        case '3':
            for i, j in company.get_companies().items():
                print(i, j)

        case '4':
            company_id = input("Enter company's ID: ")
            try:
                deleted_company = company.delete_company(int(company_id))
            except UserException:
                print("Cannot delete")
            else:
                print(deleted_company)

        case _:
            flag = False
