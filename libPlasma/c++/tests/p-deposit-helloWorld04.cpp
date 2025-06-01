
#include "libPlasma/c++/Pool.h"
#include "libPlasma/c++/Protein.h"
#include "libPlasma/c++/Hose.h"
#include "libLoam/c++/Str.h"
#include "libLoam/c++/ObRetort.h"

#include <iostream>
#include <memory>
#include <cstring>

using namespace oblong::plasma;
using namespace oblong::loam;
using namespace std;

static Slaw extract_slaw(const string &arg) {
    size_t colon_pos = arg.find(':');
    if (colon_pos == string::npos) {
        cerr << "error: ingest '" << arg << "' needs a colon to separate key and value" << endl;
        exit(EXIT_FAILURE);
    }

    Str keystr(arg.substr(0, colon_pos).c_str());
    Slaw key = Slaw::FromString(keystr);

    Slaw value;
    string valuestr = arg.substr(colon_pos + 1);
    char *endptr;
    int64 int_val = strtol(valuestr.c_str(), &endptr, 10);
    if (*endptr == '\0') {
        value = Slaw(int_val);
    } else {
        float64 float_val = strtod(valuestr.c_str(), &endptr);
        if (*endptr == '\0') {
            value = Slaw(float_val);
        } else {
            Str valstr(valuestr.c_str());
            value = Slaw::FromString(valstr);
        }
    }

    return Slaw::Cons(key, value);
}

int main() {
    const char *pool_name = "tcp://localhost/hello";
    ObRetort ret;

    unique_ptr<Hose> hose(Pool::Participate(pool_name, &ret));
    if (!hose || ret != OB_OK) {
        cerr << "Failed to connect to pool: " << pool_name << endl;
        return 1;
    }

    Slaw descrips = Slaw::List(Slaw("hello"));
    Slaw ingests = Slaw::Map(Slaw("name"), Slaw("world"));

    Protein prot(descrips, ingests);

    if (true) { // verbose
        cerr << "depositing in " << pool_name << endl;
        prot.ToSlaw().Spew(stderr);
    }

    ret = hose->Deposit(prot);

    if (ret != OB_OK) {
        cerr << "no luck on the deposit: " << ob_error_string(ret.NumericRetort()) << endl;
        return 1;
    }

    hose->Withdraw();

    cerr << "pre-delete" << endl;
    //prot->Delete();
    cerr << "post-delete" << endl;

    return 0;
}
