
// C++ version of p-deposit-helloWorld2.c, as auto-ported by CoPilot
// Deposits a protein into a pool using libPlasma++

#include "libPlasma/c++/Pool.h"
#include "libPlasma/c++/Protein.h"
#include "libLoam/c++/Str.h"
#include "libLoam/c++/ObRetort.h"

#include <iostream>
#include <memory>
#include <cstring>
#include <cstdlib>

using namespace oblong::plasma;
using namespace oblong::loam;

static Slaw extract_slaw(const char *arg)
{
    const char *colon = strchr(arg, ':');
    if (!colon)
    {
        std::cerr << "error: ingest '" << arg << "' needs a colon to separate key and value" << std::endl;
        exit(EXIT_FAILURE);
    }

    std::string keystr(arg, colon - arg);
    Slaw key = Slaw::Make(keystr.c_str());

    Slaw value;
    char *endptr;
    int64_t int_val = strtol(colon + 1, &endptr, 10);
    if (*endptr == '\0')
    {
        value = Slaw::Make(int_val);
    }
    else
    {
        double float_val = strtod(colon + 1, &endptr);
        if (*endptr == '\0')
        {
            value = Slaw::Make(float_val);
        }
        else
        {
            value = Slaw::Make(colon + 1);
        }
    }

    return Slaw::Cons(key, value);
}

int main()
{
    const char *dstr = "hello";
    const char *istr = "name:world";
    const char *pnstr = "tcp://localhost/hello";

    ObRetort ret;
    std::unique_ptr<Pool> pool(Pool::Participate(pnstr, &ret));
    if (!pool || ret != OB_OK)
    {
        std::cerr << "Failed to connect to pool: " << pnstr << std::endl;
        return 1;
    }

    Slaw descrips = Slaw::List(dstr);
    Slaw ingest = extract_slaw(istr);
    Slaw ingests = Slaw::List(ingest);

    Protein prot = Protein::From(descrips, ingests);
    std::cerr << "depositing in " << pnstr << std::endl;
    prot.SpewOverview(stderr);

    ret = pool->Deposit(prot);
    if (ret != OB_OK)
    {
        std::cerr << "no luck on the deposit: " << ob_error_string(ret.NumericRetort()) << std::endl;
        return pool_cmd_retort_to_exit_code(ret);
    }

    pool->Withdraw();
    return 0;
}

/// end ///
