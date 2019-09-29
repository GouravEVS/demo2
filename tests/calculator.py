#!/usr/bin/env python3



def main():
    from calculator.software.calc_software import software_addition , software_subtract , software_multiply , software_division
    from calculator.hardware.calc_hardware import hardware_addition , hardware_subtract , hardware_multiply , hardware_division
    print(software_addition(10,5))
    print(software_subtract(10,5))
    print(software_multiply(10,5))
    print(software_division(10,5))
    print(hardware_addition(10,5))
    print(hardware_subtract(10,5))
    print(hardware_multiply(10,5))
    print(hardware_division(10,5))
    print('import is working')


if __name__ == '__main__':
    main()
