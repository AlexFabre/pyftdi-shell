import sys
from i2c_shell import I2CShell
from spi_shell import SPIShell
from gpio_shell import GPIOShell
import argparse

try:
    import readline  # Import readline for command history navigation
except ImportError:
    print("Module 'readline' is required for command history navigation.")

def main():
    parser = argparse.ArgumentParser(description='''
                                     FTDI Interface Console.
                                     ''')
    parser.add_argument('function', type=str, help='Function type', choices=['i2c', 'spi', 'gpio'])
    parser.add_argument('ftdi_url', type=str, help='''
                        FTDI channel URL (e.g., ftdi:///2)
                        (See official PyFtdi documentation for URL format
                        https://eblot.github.io/pyftdi/urlscheme.html)
                        ''')

    args = parser.parse_args()

    if args.function == "i2c":
        shell = I2CShell(args.ftdi_url)
    elif args.function == "spi":
        shell = SPIShell(args.ftdi_url)
    elif args.function == "gpio":
        shell = GPIOShell(args.ftdi_url, 0xFF)

    shell.run()
    

if __name__ == '__main__':
    main()
