from string import Template


def main():
    #String Formating with format
    print("Hello I am {0} from {1}".format('Saman', 'Kathmandu'))

    #create a template using placeholder
    temp = Template("Hello I am ${name} from ${address}")

    #substitue the value in template
    str1 = temp.substitute(name="Saman", address="Kathmandu")
    print(str1)

    #use dictionary to substitute the value
    data = {
        "name" : "Saman",
        "address" : "Kathmandu"
    }

    str2 = temp.substitute(data)
    print(str2)


#if this module is called on it's own then __name__ = __main__ 
#if this module is called by another module then __name__ = calling module name
if __name__ == "__main__":
    main()