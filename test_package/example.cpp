// Taken from argh's repository itself for convenience: https://github.com/adishavit/argh/blob/master/test_package/test_package.cpp
#include <iostream>

#include <argh.h>

int main(int argc, char* argv[])
{
    argh::parser cmdl;
    cmdl.parse(argc, argv, argh::parser::PREFER_PARAM_FOR_UNREG_OPTION);

    if (cmdl["-v"])
        std::cout << "Verbose, I am." << std::endl;

    return EXIT_SUCCESS;
}
