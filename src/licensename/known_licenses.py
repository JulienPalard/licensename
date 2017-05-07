import re

KNOWN_FIRST_LINES = {
    "\"the beer-ware license\" (revision 42): <phk@freebsd.org> wrote this file. as long as you retain this notice you can do whatever you want with this stuff. if we meet some day, and you think this stuff is worth it, you can buy me a beer in return poul-henning kamp": "Beerware",
    "(1) redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.": "BSD-3-Clause-LBNL",
    "part 1: cmu/ucd copyright notice: (bsd like) -----": "Net-SNMP",
    "this license agreement is between the corporation for national research initiatives, having an office at 1895 preston white drive, reston, va 20191 (\"cnri\"), and the individual or organization (\"licensee\") accessing and using jpython version 1.1.x in source or binary form and its associated documentation as provided herein (\"software\").": "CNRI-Jython",
    "you may make and give away verbatim copies of the source form of the software without restriction, provided that you duplicate all of the original copyright notices and associated disclaimers.": "Ruby",
    "you can do what you want with it": "diffmark",
    "3dfx glide source code general public license": "Glide",
    "a modified version of this file may be distributed, but it should be distributed with a *different* name. changed files must be distributed *together with a complete and unchanged* distribution of these files.": "dvipdfm",
    "a world-wide, royalty-free, non-exclusive right to distribute, copy, modify, create derivatives, and use, in source and binary forms, is hereby granted, subject to acceptance of this license. performance of any of the aforementioned acts indicates acceptance to be bound by the following terms and conditions:": "AMPAS",
    "acpi - software license agreement": "Intel-ACPI",
    "adaptive public license": {
        "version 1.0": "APL-1.0"
    },
    "affero general public license": {
        "version 1, march 2002 copyright (c) 2002 affero inc. 510 third street - suite 225, san francisco, ca 94107, usa": "AGPL-1.0"
    },
    "antlr 2 license": "ANTLR-PD",
    "apple public source license": {
        "version 1.0 - march 16, 1999": "APSL-1.0",
        "version 1.1 - april 19,1999": "APSL-1.1",
        "version 2.0 - august 6, 2003": "APSL-2.0"
    },
    "academic free license": {
        "version 1.1": "AFL-1.1",
        "version 1.2": "AFL-1.2"
    },
    "academic free license (\"afl\") v. 3.0": "AFL-3.0",
    "adobe systems incorporated(r) source code license agreement": "Adobe-2006",
    "aladdin free public license": {
        "(version 8, november 18, 1999)": "Aladdin"
    },
    "allegro 4 (the giftware license)": "Giftware",
    "apache license version 2.0, january 2004 http://www.apache.org/licenses/": "Apache-2.0",
    "apache license": {
        "Version 2.0, January 2004": "Apache-2.0"
    },
    "apache license 1.1": "Apache-1.1",
    "apple public source license ver. 1.2": "APSL-1.2",
    "attribution assurance license": "AAL",
    "bsd protection license": {
        "february 2002": "BSD-Protection"
    },
    "bsd-4-clause (university of california-specific)": "BSD-4-Clause-UC",
    "before we get to the text of the license, lets just review what the license says in simple terms:": "ImageMagick",
    "bison exception": "deprecated_GPL-2.0-with-bison-exception",
    "bittorrent open source license": {
        "version 1.0": "BitTorrent-1.0",
        "version 1.1": "BitTorrent-1.1"
    },
    "boost software license - version 1.0 - august 17th, 2003": "BSL-1.0",
    "cnri open source gpl-compatible license agreement": "CNRI-Python-GPL-Compatible",
    "cnri open source license agreement": "CNRI-Python",
    "common development and distribution license (cddl)": {
        "version 1.0": "CDDL-1.0",
        "version 1.1": "CDDL-1.1"
    },
    "contrat de licence de logiciel libre cecill": {
        "avertissement": {
            "version 1 du 21/06/2004": "CECILL-1.0",
            "version 2.0 du 2006-09-05.": "CECILL-2.0"
        },
        "version 2.1 du 2013-06-21": "CECILL-2.1"
    },
    "contrat de licence de logiciel libre cecill-b": "CECILL-B",
    "contrat de licence de logiciel libre cecill-c": "CECILL-C",
    "copyright and permission notice": "curl",
    "copyright notice": "Bahyph",
    "copyright notification": "DSDP",
    "cua office public license version 1.0": "CUA-OPL-1.0",
    "caldera international, inc. hereby grants a fee free license that includes the rights use, modify and distribute this named source code, including creating derived binary products created from the source code. the source code for which caldera international, inc. grants rights are limited to the following unix operating systems that operate on the 16-bit pdp-11 cpu and early versions of the 32-bit unix operating system, with specific exclusion of unix system iii and unix system v and successor operating systems:": "Caldera",
    "code derived from the document": {
        "haskell 2010": "HaskellReport"
    },
    "common public attribution license version 1.0 (cpal)": "CPAL-1.0",
    "common public attribution license version 1.0 (cpal-1.0)": "CPAL-1.0",
    "common public license version 1.0": "CPL-1.0",
    "computer associates trusted open source license": {
        "version 1.1": "CATOSL-1.1"
    },
    "condor public license": "Condor-1.1",
    "copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. this file is offered as-is, without any warranty.": "FSFAP",
    "creative commons": {
        "attribution 1.0": "CC-BY-1.0",
        "attribution 2.0": "CC-BY-2.0",
        "attribution 2.5": "CC-BY-2.5",
        "attribution 3.0 unported": "CC-BY-3.0",
        "attribution 4.0 international": "CC-BY-4.0",
        "attribution-noderivatives 4.0 international": "CC-BY-ND-4.0",
        "attribution-noderivs 1.0": "CC-BY-ND-1.0",
        "attribution-noderivs 2.0": "CC-BY-ND-2.0",
        "attribution-noderivs 2.5": "CC-BY-ND-2.5",
        "attribution-noderivs 3.0 unported": "CC-BY-ND-3.0",
        "attribution-noderivs-noncommercial 1.0": "CC-BY-NC-ND-1.0",
        "attribution-noncommercial 1.0": "CC-BY-NC-1.0",
        "attribution-noncommercial 2.0": "CC-BY-NC-2.0",
        "attribution-noncommercial 2.5": "CC-BY-NC-2.5",
        "attribution-noncommercial 3.0 unported": "CC-BY-NC-3.0",
        "attribution-noncommercial 4.0 international": "CC-BY-NC-4.0",
        "attribution-noncommercial-noderivatives 4.0 international": "CC-BY-NC-ND-4.0",
        "attribution-noncommercial-noderivs 2.0": "CC-BY-NC-ND-2.0",
        "attribution-noncommercial-noderivs 2.5": "CC-BY-NC-ND-2.5",
        "attribution-noncommercial-noderivs 3.0 unported": "CC-BY-NC-ND-3.0",
        "attribution-noncommercial-sharealike 1.0": "CC-BY-NC-SA-1.0",
        "attribution-noncommercial-sharealike 2.0": "CC-BY-NC-SA-2.0",
        "attribution-noncommercial-sharealike 2.5": "CC-BY-NC-SA-2.5",
        "attribution-noncommercial-sharealike 3.0 unported": "CC-BY-NC-SA-3.0",
        "attribution-noncommercial-sharealike 4.0 international": "CC-BY-NC-SA-4.0",
        "attribution-sharealike 1.0": "CC-BY-SA-1.0",
        "attribution-sharealike 2.0": "CC-BY-SA-2.0",
        "attribution-sharealike 2.5": "CC-BY-SA-2.5",
        "attribution-sharealike 3.0 unported": "CC-BY-SA-3.0",
        "attribution-sharealike 4.0 international": "CC-BY-SA-4.0",
        "cc0 1.0 universal": "CC0-1.0"
    },
    "crystal stacker is freeware. this means you can pass copies around freely provided you include this document in it's original form in your distribution. please see the \"contacting us\" section of this document if you need to contact us for any reason.": "CrystalStacker",
    "cube game engine source code, 20 dec 2003 release.": "Cube",
    "do what the fuck you want to public license": {
        "version 2, december 2004": "WTFPL"
    },
    "derivative work - 1996, 1998-2000 copyright 1996, 1998-2000 the regents of the university of california": "MIT-CMU",
    "deutsche freie software lizenz": "D-FSL-1.0",
    "development of this software was funded, in part, by cray research inc., uunet communications services inc., sun microsystems inc., and scriptics corporation, none of whom are responsible for the results. the author thanks all of them.": "Spencer-99",
    "egenix.com public license agreement": {
        "version 1.1.0": "eGenix"
    },
    "erlang public license version 1.1": "ErlPL-1.1",
    "eu datagrid software license": "EUDatagrid",
    "eclipse public license - v 1.0": "EPL-1.0",
    "educational community license": {
        "version 2.0, april 2007": "ECL-2.0"
    },
    "eiffel forum license,": {
        "version 1": "EFL-1.0",
        "version 2": "EFL-2.0"
    },
    "entessa public license version. 1.0": "Entessa",
    "european union public licence": {
        "v. 1.1": "EUPL-1.1",
        "v.1.0": "EUPL-1.0"
    },
    "free software licensing agreement cecill": "CECILL-1.1",
    "cecill free software license agreement": {
        "version 2.1 dated 2013-06-21": "CECILL-2.1"
    },
    "fair license": "Fair",
    "freeimage public license - version 1.0": "FreeImage",
    "gl2ps license version 2, november 2003": "GL2PS",
    "gnu affero general public license": {
        "version 3, 19 november 2007": "AGPL-3.0"
    },
    "gnu free documentation license": {
        "version 1.1, march 2000": "GFDL-1.1",
        "version 1.2, november 2002": "GFDL-1.2",
        "version 1.3, 3 november 2008": "GFDL-1.3"
    },
    "gnu general public license": {
        "version 1, february 1989": "GPL-1.0",
        "version 2, june 1991": "GPL-2.0",
        "version 3, 29 june 2007": "GPL-3.0"
    },
    "gnu lesser general public license": {
        "version 2.1, february 1999": "LGPL-2.1",
        ".*version 3, 29 june 2007": "LGPL-3.0"
    },
    "gnu library general public license": {
        "version 2, june 1991": "LGPL-2.0",
        "version 2.1, february 1999": "LGPL-2.1"
    },
    "historical permission notice and disclaimer": "HPND",
    "ibm public license version 1.0": "IPL-1.0",
    "icu license - icu 1.8.1 and later": "ICU",
    "important: this apple software is supplied to you by apple computer, inc. (\"apple\") in consideration of your agreement to the following terms, and your use, installation, modification or redistribution of this apple software constitutes acceptance of these terms. if you do not agree with these terms, please do not use, install, modify or redistribute this apple software.": "AML",
    "interbase public license": {
        "version 1.0": "Interbase-1.0"
    },
    "ipa font license agreement v1.0": "IPA",
    "imlib2 license": "Imlib2",
    "independent jpeg group license": "IJG",
    "info-zip license": "Info-ZIP",
    "intel open source license": "Intel",
    "json license": "JSON",
    "jasper license version 2.0": "JasPer-2.0",
    "license for the extreme! lab pullparser": "xpp",
    "latex project public license": "LPPL-1.0",
    "lesser general public license for linguistic resources": "LGPLLR",
    "licence art libre": {
        " [ copyleft attitude ]": {
            "version 1.2": "LAL-1.2"
        }
    },
    "licence art libre 1.3 (lal 1.3)": "LAL-1.3",
    "licence libre du quebec - permissive (liliq-p)": "LiLiQ-P-1.1",
    "licence libre du quebec - reciprocite (liliq-r)": "LiLiQ-R-1.1",
    "licence libre du quebec - reciprocite forte (liliq-r+)": "LiLiQ-Rplus-1.1",
    "licence version 2": "Eurosym",
    "license to copy and use this software is granted provided that it is identified as the \"rsa data security, inc. .* message-digest algorithm\" in all material mentioning or referencing this software or this function.": "RSA-MD",
    "lucent public license": {
        "version 1.0": "LPL-1.0",
        "version 1.02": "LPL-1.02"
    },
    "motosoto open source license - version 0.9.1": "Motosoto",
    "makeindex distribution notice": "MakeIndex",
    "microsoft public license (ms-pl)": "MS-PL",
    "microsoft reciprocal license (ms-rl)": "MS-RL",
    "miros license": "MirOS",
    "mozilla public license": {
        "version 1.0": "MPL-1.0",
        "version 1.1": "MPL-1.1",
        "version 2.0": "MPL-2.0"
    },
    "multics license": "Multics",
    "nasa open source agreement version 1.3": "NASA-1.3",
    "naumen public license": "Naumen",
    "nethack general public license": "NGPL",
    "netizen open source license": {
        "version 1.0": "NOSL"
    },
    "netscape public license version 1.0": "NPL-1.0",
    "no limit public license": "NLPL",
    "nrl license": "NRL",
    "ntp license (ntp)": "NTP",
    "netscape public license version 1.1": "NPL-1.1",
    "nokia open source license (nokos license)": "Nokia",
    "non-profit open software license 3.0": "NPOSL-3.0",
    "norwegian licence for open government data (nlod)": "NLOD-1.0",
    "noweb is copyright 1989-2000 by norman ramsey. all rights reserved.": "Noweb",
    "oclc research public license 2.0": "OCLC-2.0",
    "odc open database license (odbl)": "ODbL-1.0",
    "open public license": {
        "version 1.0": "OPL-1.0"
    },
    "original license: this software is": "xinetd",
    "oset public license": "OSET-PL-2.1",
    "open cascade technology public license": {
        "version 6.6, april 2013": "OCCT-PL"
    },
    "open data commons - public domain dedication & license (pddl)": "PDDL-1.0",
    "open software license v. 3.0 (osl-3.0)": "OSL-3.0",
    "open software licensev. 2.0": "OSL-2.0",
    "openssl license": "OpenSSL",
    "ps utilities package": "psutils",
    "python software foundation license version 2": "Python-2.0",
    "permission is granted to anyone to use this software for any purpose on any computer system, and to redistribute it freely, subject to the following restrictions:": {
        "the author is not responsible for the consequences of use of this software, no matter how awful, even if they arise from defects in it.": "Spencer-86",
        "this software is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose.": "Newsletr"
    },
    "permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies.": "Latex2e",
    "permission is hereby granted, free of charge, to any person obtaining a copy of this documentation file to use, copy, publish, distribute, sublicense, and/or sell copies of the documentation, and to permit others to do the same, provided that:": "Adobe-Glyph",
    "permission is hereby granted, free of charge, to any person obtaining": {
        "the above copyright notice and this permission notice shall be included in all copies of the software and its copyright notices. in addition publicly documented acknowledgment must be given that this software has been used if no source code of this software is made available publicly. this includes acknowledgments in either copyright notices, manuals, publicity and marketing documents or any documentation provided with any product containing this software. this license does not apply to any software that links to the libraries provided by this software (statically or dynamically), but only to the software provided.": "MIT-enna",
        "the above copyright notice and this permission notice shall be included in all copies of the software and its documentation and acknowledgment shall be given in the documentation and software packages that this software was used.": "MIT-feh",
        "the above copyright notice and this permission notice shall be included in all copies of the software, its documentation and marketing & publicity materials, and acknowledgment shall be given in the documentation, materials and software packages that this software was used.": "MIT-advertising",
        "the above copyright notice and this permission notice shall be included": {
            "distributions of all or part of the software intended to be used by the recipients as they would use the unmodified software, containing modifications that substantially alter, remove, or disable functionality of the software, outside of the documented configuration mechanisms provided by the software, shall be modified such that the original author's bug reporting email addresses and urls are either replaced with the contact information of the parties responsible for the changes, or removed entirely.": "MITNFA",
            "the software is provided .as is., without warranty of any kind": "MIT",
            "the software is provided \"as is\", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. in no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.": "MIT"
        }
    },
    "permission to use, copy, and distribute this software and its documentation for any purpose with or without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation.": "gnuplot",
    "permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.": "0BSD",
    "permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that (i) the above copyright notices and this permission notice appear in all copies of the software and related documentation, and (ii) the names of sam leffler and silicon graphics may not be used in any advertising or publicity relating to the software without the specific, prior written permission of sam leffler and silicon graphics.": "libtiff",
    "portions of this software were developed by the unidata program at the university corporation for atmospheric research.": "NetCDF",
    "postgresql database management system": "PostgreSQL",
    "rdisc (this program) was developed by sun microsystems, inc. and is provided for unrestricted use provided that this legend is included on all tape media and as a part of the software program in whole or part. users may copy or modify rdisc without charge, and they may freely distribute it.": "Rdisc",
    "realnetworks public source license version 1.0": "RPSL-1.0",
    "reciprocal public license 1.5 (rpl1.5)": "RPL-1.5",
    "reciprocal public license, version 1.1": "RPL-1.1",
    "red hat ecos public license v1.1": "RHeCos-1.1",
    "redistribution and use in any form of this material and any product thereof including software in source or binary forms, along with any related documentation, with or without modification (\"this material\"), is permitted provided that the following conditions are met:": "AMDPLPA",
    "redistribution and use in source and binary forms, with or without": {
        "redistribution of source code must retain the above copyright notice, this list of conditions and the following disclaimer.": "BSD-3-Clause-No-Nuclear",
        "redistributions of source code must retain the above copyright notice": {
            "redistributions in binary form must reproduce the above copyright": {
                "all advertising materials mentioning features or use of this software must display the following acknowledgement:": "BSD-4-Clause",
                "all advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by the .*": "BSD-4-Clause",
                "all advertising materials mentioning features or use of this software must display the following acknowledgment: \"this product includes software developed by the .*.\"": "Apache-1.0",
                "any additions, deletions, or changes to the original files must be clearly indicated": "Mup",
                "neither the name of": {
                    "this software is provided": "BSD-3-Clause",
                    "redistributions of any form whatsoever must retain the following acknowledgment: 'this product includes software developed by the .*": "BSD-3-Clause-Attribution",
                },
                "redistributions in any form must be accompanied by information on how to obtain complete source code for the db software and any accompanying software that uses the db software. the source code must either be included in the distribution or be available for no more than the cost of distribution plus a nominal fee, and must be freely redistributable under reasonable conditions. for an executable file, complete source code means the source code for all modules it contains. it does not include source code for modules or files that typically accompany the major components of the operating system on which the executable file runs.": "Sleepycat",
                "redistributions in any form must be accompanied by information on how to obtain complete source code for this software and any accompanying software that uses this software. the source code must either be included in the distribution or be available in a timely fashion for no more than the cost of distribution plus a nominal fee, and must be freely redistributable under reasonable and no more restrictive conditions. for an executable file, complete source code means the source code for all modules it contains. it does not include source code for modules or files that typically accompany the major components of the operating system on which the executable file runs.": "TOSL",
                "this software is provided by": "BSD-2-Clause",
            },
            "the origin of this software must not be misrepresented; you must not claim that you wrote the original software. if you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.": "bzip2-1.0.6"
        }
    },
    "redistribution and use of this software and associated documentation (\"software\"), with or without modification, are permitted provided that the following conditions are met:": "Plexus",
    "redistribution and use of this software in source and binary forms, with or without modification, are permitted provided that the following conditions are met:": "BSD-Source-Code",
    "ricoh source code public license": {
        "version 1.0": "RSCPL"
    },
    "sax is free!": "SAX-PD",
    "scea shared source license 1.0": "SCEA",
    "sendmail license": "Sendmail",
    "sgi free software license b": {
        "(version 1.0 1/25/2000)": "SGI-B-1.0",
        "(version 1.1 02/22/2000)": "SGI-B-1.1",
        "(version 2.0, sept. 18, 2008)": "SGI-B-2.0"
    },
    "sil open font license": {
        "version 1.0 - 22 november 2005": "OFL-1.0",
        "version 1.1 - 26 february 2007": "OFL-1.1"
    },
    "standard ml of new jersey copyright notice, license and disclaimer.": "SMLNJ",
    "storage networking industry association": {
        "version 1.1": "SNIA"
    },
    "sugarcrm public license": "SugarCRM-1.1.3",
    "sun industry standards source license": {
        "version 1.2": "SISSL-1.2"
    },
    "sun public license version 1.0": "SPL-1.0",
    "secure messaging protocol (smp) libraries [acl, cml, sfl]": "SMPPL",
    "simple public license (simpl)": "SimPL-2.0",
    "software license for mtl": "MTLL",
    "sun industry standards source license - version 1.1": "SISSL",
    "sybase open watcom public license version 1.0": "Watcom-1.0",
    "the frameworx open license 1.0": "Frameworx-1.0",
    "the q public license version 1.0": "QPL-1.0",
    "torque v2.5+ software license v1.1": "TORQUE-1.1",
    "the \"artistic license\"": "Artistic-1.0-Perl",
    "the academic free license": {
        "v. 2.0": "AFL-2.0",
        "v.2.1": "AFL-2.1"
    },
    "the artistic license": "Artistic-1.0",
    "the artistic license 2.0": "Artistic-2.0",
    "the clarified artistic license": "ClArtistic",
    "the clear bsd license": "BSD-3-Clause-Clear",
    "the code project open license (cpol) 1.02": "CPOL-1.02",
    "the educational community license": "ECL-1.0",
    "the freebsd copyright": "BSD-2-Clause-FreeBSD",
    "the freetype project license": "FTL",
    "the latex project public license": {
        "lppl version 1.1 1999-07-10": "LPPL-1.1",
        "lppl version 1.2 1999-09-03": "LPPL-1.2",
        "lppl version 1.3a 2004-10-01": "LPPL-1.3a",
        "lppl version 1.3c 2008-05-04": "LPPL-1.3c"
    },
    "the national science and technology research center for computation and visualization of geometric structures (the geometry center) university of minnesota": "Qhull",
    "the net boolean public license": "NBPL-1.0",
    "the open group test suite license": "OGTSL",
    "the open software license": {
        "v. 1.0": "OSL-1.0",
        "v. 1.1": "OSL-1.1",
        "v. 2.1": "OSL-2.1"
    },
    "the openldap public license": {
        "version 1.1, 25 august 1998": "OLDAP-1.1",
        "version 1.2, 1 september 1998": "OLDAP-1.2",
        "version 1.3, 17 january 1999": "OLDAP-1.3",
        "version 1.4, 18 january 1999": "OLDAP-1.4",
        "version 2.0, 7 june 1999": "OLDAP-2.0",
        "version 2.0.1, 21 december 1999": "OLDAP-2.0.1",
        "version 2.1, 29 february 2000": "OLDAP-2.1",
        "version 2.2, 1 march 2000": "OLDAP-2.2",
        "version 2.2.1, 1 march 2000": "OLDAP-2.2.1",
        "version 2.2.2, 28 july 2000": "OLDAP-2.2.2",
        "version 2.3, 28 july 2000": "OLDAP-2.3",
        "version 2.4, 8 december 2000": "OLDAP-2.4",
        "version 2.5, 11 may 2001": "OLDAP-2.5",
        "version 2.6, 14 june 2001": "OLDAP-2.6",
        "version 2.7, 7 september 2001": "OLDAP-2.7",
        "version 2.8, 17 august 2003": "OLDAP-2.8"
    },
    "the php license,": {
        "version 3.0": "PHP-3.0",
        "version 3.01": "PHP-3.01"
    },
    "the sfl license agreement": "iMatix",
    "the tmate open source license.": "TMate",
    "the universal permissive license (upl), version 1.0": "UPL-1.0",
    "the x.net, inc. license": "Xnet",
    "the zend engine license, version 2.00": "Zend-2.0",
    "the authors hereby grant permission to use, copy, modify, distribute, and license this software and its documentation for any purpose, provided that existing copyright notices are retained in all copies and that this notice is included verbatim in any distributions. no written agreement, license, or royalty fee is required for any of the authorized uses. modifications to this software may be copyrighted by their authors and need not follow the licensing terms described here, provided that the new terms are clearly indicated on the first page of each file where they apply.": "SWL",
    "the bsd-2 license": "BSD-2-Clause",
    "the ecos license version 2.0": "deprecated_eCos-2.0",
    "the source code in this package is copyright 1999-2010 by andrew plotkin.": "Glulxe",
    "this fastcgi application library source and object code (the \"software\") and its documentation (the \"documentation\") are copyrighted by open market, inc (\"open market\"). the following terms apply to all files associated with the software and documentation unless explicitly disclaimed in individual files.": "OML",
    "this code is derived from software contributed to the netbsd foundation by .*": "BSD-2-Clause-NetBSD",
    "this configure script is free software; the free software foundation gives unlimited permission to copy, distribute and modify it.": "FSFUL",
    "this copy of the libpng notices is provided for your convenience. in case of any discrepancy between this copy and the notices in the file png.h that is included in the libpng distribution, the latter shall prevail.": "Libpng",
    "this file and the 14 postscript(r) afm files it accompanies may be used, copied, and distributed for any purpose and without charge, with or without modification, provided that all copyright notices are retained; that the afm files are not distributed without this file; that all modifications to this file or any of the afm files are prominently noted in the modified file(s); and that this paragraph is not modified. adobe systems has no responsibility or obligation to support the use of the afm files.": "APAFML",
    "this file is free software; the free software foundation gives unlimited permission to copy and/or distribute it, with or without modifications, as long as this notice is preserved.": "FSFULLR",
    "this file may be freely copied and redistributed as long as:": "Afmparse",
    "this file may be freely transmitted and reproduced, but it may not be changed unless the name is changed also (except that you may freely change the paper-size option for \\documentclass).": "Dotseqn",
    "this file was added by clea f. rees on 2008/11/30 with the permission of dean guenther and pointers to this file were added to all source files.": "Wsuipa",
    "this is apreambl.tex, version 1.10e, written by hans-hermann bode": "Abstyles",
    "this is a package of commutative diagram macros built on top of xy-pic by michael barr (email: barr@barrs.org). its use is unrestricted. it may be freely distributed, unchanged, for non-commercial or commercial use. if changed, it must be renamed. inclusion in a commercial software package is also permitted, but i would appreciate receiving a free copy for my personal examination and use. there are no guarantees that this package is good for anything. i have tested it with latex 2e, latex 2.09 and plain tex. although i know of no reason it will not work with amstex, i have not tested it.": "Barr",
    "this is free and unencumbered software released into the public domain.": "Unlicense",
    "this material was originally written and compiled by wietse venema at eindhoven university of technology, the netherlands, in 1990, 1991, 1992, 1993, 1994 and 1995.": "TCP-wrappers",
    "this program is free software; you can redistribute it freely.": {
        "use it at your own risk; there is no warranty.": "XSkat"
    },
    "this program is free software: you can redistribute it and/or modify": {
        ".*either version 3": "GPL-3.0"
    },
    "this software is copyrighted by .* and other parties. the following terms apply to all files associated with the software unless explicitly disclaimed in individual files.": "TCL",
    "this software is distributed in the hope that it will be useful, but with no warranty of any kind.": "Leptonica",
    "this software is not subject to any license of the american telephone and telegraph company or of the regents of the university of california.": "Spencer-94",
    "this software is provided 'as-is', without any express or implied warranty. in no event will the authors be held liable for any damages arising from the use of this software.": {
        "permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:": "zlib-like",
    },
    "this source code has been made available to you by ibm on an as-is basis. anyone receiving this source is licensed under ibm copyrights to use it in any way he or she deems fit, including copying it, modifying it, compiling it, and redistributing it either with or without modifications. no license under ibm patents or patent applications is to be implied by the copyright license.": "IBM-pibs",
    "this work is being provided by the copyright holders under the following license.": "W3C-20150513",
    "unicode, inc. license agreement - data files and software": {
        "unicode data files include all data files under the directories http://www.unicode.org/public/, http://www.unicode.org/reports/, and http://www.unicode.org/cldr/data/. unicode data files do not include pdf online code charts under the directory http://www.unicode.org/public/. software includes any source code published in the unicode standard or under the directories http://www.unicode.org/public/, http://www.unicode.org/reports/, and http://www.unicode.org/cldr/data/.": "Unicode-DFS-2015",
        "unicode data files include all data files under the directories http://www.unicode.org/public/, http://www.unicode.org/reports/, http://www.unicode.org/cldr/data/, http://source.icu-project.org/repos/icu/, and http://www.unicode.org/utility/trac/browser/.": "Unicode-DFS-2016"
    },
    "unicode terms of use": "Unicode-TOU",
    "university of illinois/ncsa open source license": "NCSA",
    "use and copying of this software and preparation of derivative works based upon this software are permitted. any copy of this software or of any derivative work must include the above copyright notice of xerox corporation, this paragraph and the one after it. any distribution of this software or derivative works must comply with all applicable united states export control laws.": "Xerox",
    "use is subject to license terms.": "BSD-3-Clause-No-Nuclear-License-2014",
    "vim license": "Vim",
    "vostrom public license for open source": "VOSTROM",
    "version 1.0.5 of 10 december 2007": "bzip2-1.0.5",
    "vovida software license v. 1.0": "VSL-1.0",
    "w3c software notice and license": "W3C",
    "w3c(r) software notice and license": "W3C-19980720",
    "x11 license": "X11",
    "xfree86 license (version 1.1)": "XFree86-1.1",
    "yahoo! public license, version 1.0 (ypl)": "YPL-1.0",
    "yahoo! public license, version 1.1 (ypl)": "YPL-1.1",
    "you can use doc software in commercial and/or binary software releases and are under no obligation to redistribute any of your source code that is built using doc software. note, however, that you may not misappropriate the doc software code, such as copyrighting it yourself or claiming authorship of the doc software code, in a way that will prevent doc software from being distributed freely using an open-source development model. you needn't inform anyone that you're using doc software in your software, though we encourage you to let us know so we can promote your project in the doc software success stories.": "DOC",
    "you may copy and distribute this file freely. any queries and complaints should be forwarded to jim.davies@comlab.ox.ac.uk.": "Zed",
    "you may freely use, modify, and/or distribute each of the files in this package without limitation. the package consists of the following files:": "Borceux",
    "zimbra public license, version 1.3 (zpl)": "Zimbra-1.3",
    "zimbra public license, version 1.4 (zpl)": "Zimbra-1.4",
    "zope public license (zpl) version 1.1": "ZPL-1.1",
    "zope public license (zpl) version 2.0": "ZPL-2.0",
    "zope public license (zpl) version 2.1": "ZPL-2.1",
    "cwpuzzle.dtx is distributed in the hope that it will be useful, but without any warranty. no author or distributor accepts responsibility to anyone for the consequences of using it or for whether it serves any particular purpose or works at all, unless he says so in writing.": "Crossword",
    "gsoap public license": "gSOAP-1.3b",
    "insert gpl v2 text here": {
        "gcc linking exception": "deprecated_GPL-2.0-with-GCC-exception",
        "font exception": "deprecated_GPL-2.0-with-font-exception"
    },
    "insert gpl v3 text here": {
        "autoconf configure script exception": "deprecated_GPL-3.0-with-autoconf-exception",
        "gcc runtime library exception": "deprecated_GPL-3.0-with-GCC-exception"
    },
    "psfrag.dtx": "psfrag",
    "wxwindows library licence, version 3.1": "deprecated_WXwindows",
    "zlib license": "Zlib",
    "insert gpl v2 license text here": {
        "autoconf exception": "deprecated_GPL-2.0-with-autoconf-exception",
        "class path exception": "deprecated_GPL-2.0-with-classpath-exception"
    },
    "licensed under the apache license, version 2.0": "Apache-2.0",
    "apache license": {
        "version 2.0": "Apache-2.0"
    },
    "permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.": "ISC",
    ".*the open source pil software license:": "PIL",
    "portions of this material resulted from work developed under a u.s. government contract": "mpich2"
}
