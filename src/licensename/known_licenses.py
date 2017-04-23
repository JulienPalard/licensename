import re

KNOWN_FIRST_LINES = {
    "\"THE BEER-WARE LICENSE\" (Revision 42): <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you can do whatever you want with this stuff. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp": "Beerware",
    "(1) Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.": "BSD-3-Clause-LBNL",
    "Part 1: CMU/UCD copyright notice: (BSD like) -----": "Net-SNMP",
    "This LICENSE AGREEMENT is between the Corporation for National Research Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191 (\"CNRI\"), and the Individual or Organization (\"Licensee\") accessing and using JPython version 1.1.x in source or binary form and its associated documentation as provided herein (\"Software\").": "CNRI-Jython",
    "You may make and give away verbatim copies of the source form of the software without restriction, provided that you duplicate all of the original copyright notices and associated disclaimers.": "Ruby",
    "you can do what you want with it": "diffmark",
    "3DFX GLIDE Source Code General Public License": "Glide",
    "A modified version of this file may be distributed, but it should be distributed with a *different* name. Changed files must be distributed *together with a complete and unchanged* distribution of these files.": "dvipdfm",
    "A world-wide, royalty-free, non-exclusive right to distribute, copy, modify, create derivatives, and use, in source and binary forms, is hereby granted, subject to acceptance of this license. Performance of any of the aforementioned acts indicates acceptance to be bound by the following terms and conditions:": "AMPAS",
    "ACPI - Software License Agreement": "Intel-ACPI",
    "ADAPTIVE PUBLIC LICENSE": {
        "Version 1.0": "APL-1.0"
    },
    "AFFERO GENERAL PUBLIC LICENSE": {
        "Version 1, March 2002 Copyright © 2002 Affero Inc. 510 Third Street - Suite 225, San Francisco, CA 94107, USA": "AGPL-1.0"
    },
    "ANTLR 2 License": "ANTLR-PD",
    "APPLE PUBLIC SOURCE LICENSE": {
        "Version 1.0 - March 16, 1999": "APSL-1.0",
        "Version 1.1 - April 19,1999": "APSL-1.1",
        "Version 2.0 - August 6, 2003": "APSL-2.0"
    },
    "Academic Free License": {
        "Version 1.1": "AFL-1.1",
        "Version 1.2": "AFL-1.2"
    },
    "Academic Free License (\u201cAFL\u201d) v. 3.0": "AFL-3.0",
    "Adobe Systems Incorporated(r) Source Code License Agreement": "Adobe-2006",
    "Aladdin Free Public License": {
        "(Version 8, November 18, 1999)": "Aladdin"
    },
    "Allegro 4 (the giftware license)": "Giftware",
    "Apache License Version 2.0, January 2004 http://www.apache.org/licenses/": "Apache-2.0",
    "Apache License": {
        "Version 2.0, January 2004": "Apache-2.0"
    },
    "Apache License 1.1": "Apache-1.1",
    "Apple Public Source License Ver. 1.2": "APSL-1.2",
    "Attribution Assurance License": "AAL",
    "BSD Protection License": {
        "February 2002": "BSD-Protection"
    },
    "BSD-4-Clause (University of California-Specific)": "BSD-4-Clause-UC",
    "Before we get to the text of the license, lets just review what the license says in simple terms:": "ImageMagick",
    "Bison Exception": "deprecated_GPL-2.0-with-bison-exception",
    "BitTorrent Open Source License": {
        "Version 1.0": "BitTorrent-1.0",
        "Version 1.1": "BitTorrent-1.1"
    },
    "Boost Software License - Version 1.0 - August 17th, 2003": "BSL-1.0",
    "CNRI OPEN SOURCE GPL-COMPATIBLE LICENSE AGREEMENT": "CNRI-Python-GPL-Compatible",
    "CNRI OPEN SOURCE LICENSE AGREEMENT": "CNRI-Python",
    "COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL)": {
        "Version 1.0": "CDDL-1.0",
        "Version 1.1": "CDDL-1.1"
    },
    "CONTRAT DE LICENCE DE LOGICIEL LIBRE CeCILL": {
        "Avertissement": {
            "Ce contrat est une licence de logiciel libre issue d'une concertation entre ses auteurs afin que le respect de deux grands principes pr\u00e9side \u00e0 sa r\u00e9daction:": "CECILL-2.0",
            "Ce contrat est une licence de logiciel libre issue d’une concertation entre ses auteurs afin que le respect de deux grands principes préside à sa rédaction:": "CECILL-1.0"
        },
        "Version 2.1 du 2013-06-21": "CECILL-2.1"
    },
    "CONTRAT DE LICENCE DE LOGICIEL LIBRE CeCILL-B": "CECILL-B",
    "CONTRAT DE LICENCE DE LOGICIEL LIBRE CeCILL-C": "CECILL-C",
    "COPYRIGHT": "mpich2",
    "COPYRIGHT AND PERMISSION NOTICE": "curl",
    "COPYRIGHT NOTICE": "Bahyph",
    "COPYRIGHT NOTIFICATION": "DSDP",
    "CUA Office Public License Version 1.0": "CUA-OPL-1.0",
    "Caldera International, Inc. hereby grants a fee free license that includes the rights use, modify and distribute this named source code, including creating derived binary products created from the source code. The source code for which Caldera International, Inc. grants rights are limited to the following UNIX Operating Systems that operate on the 16-Bit PDP-11 CPU and early versions of the 32-Bit UNIX Operating System, with specific exclusion of UNIX System III and UNIX System V and successor operating systems:": "Caldera",
    "Code derived from the document \"Report on the Programming Language Haskell 2010\", is distributed under the following license:": "HaskellReport",
    "Common Public Attribution License Version 1.0 (CPAL)": "CPAL-1.0",
    "Common Public License Version 1.0": "CPL-1.0",
    "Computer Associates Trusted Open Source License": {
        "Version 1.1": "CATOSL-1.1"
    },
    "Condor Public License": "Condor-1.1",
    "Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.": "FSFAP",
    "Creative Commons": {
        "Attribution 1.0": "CC-BY-1.0",
        "Attribution 2.0": "CC-BY-2.0",
        "Attribution 2.5": "CC-BY-2.5",
        "Attribution 3.0 Unported": "CC-BY-3.0",
        "Attribution 4.0 International": "CC-BY-4.0",
        "Attribution-NoDerivatives 4.0 International": "CC-BY-ND-4.0",
        "Attribution-NoDerivs 1.0": "CC-BY-ND-1.0",
        "Attribution-NoDerivs 2.0": "CC-BY-ND-2.0",
        "Attribution-NoDerivs 2.5": "CC-BY-ND-2.5",
        "Attribution-NoDerivs 3.0 Unported": "CC-BY-ND-3.0",
        "Attribution-NoDerivs-NonCommercial 1.0": "CC-BY-NC-ND-1.0",
        "Attribution-NonCommercial 1.0": "CC-BY-NC-1.0",
        "Attribution-NonCommercial 2.0": "CC-BY-NC-2.0",
        "Attribution-NonCommercial 2.5": "CC-BY-NC-2.5",
        "Attribution-NonCommercial 3.0 Unported": "CC-BY-NC-3.0",
        "Attribution-NonCommercial 4.0 International": "CC-BY-NC-4.0",
        "Attribution-NonCommercial-NoDerivatives 4.0 International": "CC-BY-NC-ND-4.0",
        "Attribution-NonCommercial-NoDerivs 2.0": "CC-BY-NC-ND-2.0",
        "Attribution-NonCommercial-NoDerivs 2.5": "CC-BY-NC-ND-2.5",
        "Attribution-NonCommercial-NoDerivs 3.0 Unported": "CC-BY-NC-ND-3.0",
        "Attribution-NonCommercial-ShareAlike 1.0": "CC-BY-NC-SA-1.0",
        "Attribution-NonCommercial-ShareAlike 2.0": "CC-BY-NC-SA-2.0",
        "Attribution-NonCommercial-ShareAlike 2.5": "CC-BY-NC-SA-2.5",
        "Attribution-NonCommercial-ShareAlike 3.0 Unported": "CC-BY-NC-SA-3.0",
        "Attribution-NonCommercial-ShareAlike 4.0 International": "CC-BY-NC-SA-4.0",
        "Attribution-ShareAlike 1.0": "CC-BY-SA-1.0",
        "Attribution-ShareAlike 2.0": "CC-BY-SA-2.0",
        "Attribution-ShareAlike 2.5": "CC-BY-SA-2.5",
        "Attribution-ShareAlike 3.0 Unported": "CC-BY-SA-3.0",
        "Attribution-ShareAlike 4.0 International": "CC-BY-SA-4.0",
        "CC0 1.0 Universal": "CC0-1.0"
    },
    "Crystal Stacker is freeware. This means you can pass copies around freely provided you include this document in it's original form in your distribution. Please see the \"Contacting Us\" section of this document if you need to contact us for any reason.": "CrystalStacker",
    "Cube game engine source code, 20 dec 2003 release.": "Cube",
    "DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE": {
        "Version 2, December 2004": "WTFPL"
    },
    "Derivative Work - 1996, 1998-2000 Copyright 1996, 1998-2000 The Regents of the University of California": "MIT-CMU",
    "Deutsche Freie Software Lizenz": "D-FSL-1.0",
    "Development of this software was funded, in part, by Cray Research Inc., UUNET Communications Services Inc., Sun Microsystems Inc., and Scriptics Corporation, none of whom are responsible for the results. The author thanks all of them.": "Spencer-99",
    "EGENIX.COM PUBLIC LICENSE AGREEMENT": {
        "Version 1.1.0": "eGenix"
    },
    "ERLANG PUBLIC LICENSE Version 1.1": "ErlPL-1.1",
    "EU DataGrid Software License": "EUDatagrid",
    "Eclipse Public License - v 1.0": "EPL-1.0",
    "Educational Community License": {
        "Version 2.0, April 2007": "ECL-2.0"
    },
    "Eiffel Forum License,": {
        "version 1": "EFL-1.0",
        "version 2": "EFL-2.0"
    },
    "Entessa Public License Version. 1.0": "Entessa",
    "European Union Public Licence": {
        "V. 1.1": "EUPL-1.1",
        "V.1.0": "EUPL-1.0"
    },
    "FREE SOFTWARE LICENSING AGREEMENT CeCILL": "CECILL-1.1",
    "Fair License": "Fair",
    "FreeImage Public License - Version 1.0": "FreeImage",
    "GL2PS LICENSE Version 2, November 2003": "GL2PS",
    "GNU AFFERO GENERAL PUBLIC LICENSE": {
        "Version 3, 19 November 2007": "AGPL-3.0"
    },
    "GNU Free Documentation License": {
        "Version 1.1, March 2000": "GFDL-1.1",
        "Version 1.2, November 2002": "GFDL-1.2",
        "Version 1.3, 3 November 2008": "GFDL-1.3"
    },
    "GNU GENERAL PUBLIC LICENSE": {
        "Version 1, February 1989": "GPL-1.0",
        "Version 2, June 1991": "GPL-2.0",
        "Version 3, 29 June 2007": "GPL-3.0"
    },
    "GNU LESSER GENERAL PUBLIC LICENSE": {
        "Version 2.1, February 1999": "LGPL-2.1",
        "Version 3, 29 June 2007": "LGPL-3.0"
    },
    "GNU LIBRARY GENERAL PUBLIC LICENSE": {
        "Version 2, June 1991": "LGPL-2.0",
        "Version 2.1, February 1999": "LGPL-2.1"
    },
    "Historical Permission Notice and Disclaimer": "HPND",
    "IBM Public License Version 1.0": "IPL-1.0",
    "ICU License - ICU 1.8.1 and later": "ICU",
    "IMPORTANT: This Apple software is supplied to you by Apple Computer, Inc. (\"Apple\") in consideration of your agreement to the following terms, and your use, installation, modification or redistribution of this Apple software constitutes acceptance of these terms. If you do not agree with these terms, please do not use, install, modify or redistribute this Apple software.": "AML",
    "INTERBASE PUBLIC LICENSE": {
        "Version 1.0": "Interbase-1.0"
    },
    "IPA Font License Agreement v1.0": "IPA",
    "Imlib2 License": "Imlib2",
    "Independent JPEG Group License": "IJG",
    "Info-ZIP License": "Info-ZIP",
    "Intel Open Source License": "Intel",
    "JSON License": "JSON",
    "JasPer License Version 2.0": "JasPer-2.0",
    "LICENSE FOR THE Extreme! Lab PullParser": "xpp",
    "LaTeX Project Public License": "LPPL-1.0",
    "Lesser General Public License For Linguistic Resources": "LGPLLR",
    "Licence Art Libre": {
        " [ Copyleft Attitude ]": {
            "Version 1.2": "LAL-1.2"
        }
    },
    "Licence Art Libre 1.3 (LAL 1.3)": "LAL-1.3",
    "Licence Libre du Qu\u00e9bec \u2013 Permissive (LiLiQ-P)": "LiLiQ-P-1.1",
    "Licence Libre du Qu\u00e9bec \u2013 R\u00e9ciprocit\u00e9 (LiLiQ-R)": "LiLiQ-R-1.1",
    "Licence Libre du Qu\u00e9bec \u2013 R\u00e9ciprocit\u00e9 forte (LiLiQ-R+)": "LiLiQ-Rplus-1.1",
    "Licence Version 2": "Eurosym",
    "License to copy and use this software is granted provided that it is identified as the \"RSA Data Security, Inc. .* Message-Digest Algorithm\" in all material mentioning or referencing this software or this function.": "RSA-MD",
    "Lucent Public License": {
        "Version 1.0": "LPL-1.0",
        "Version 1.02": "LPL-1.02"
    },
    "MOTOSOTO OPEN SOURCE LICENSE - Version 0.9.1": "Motosoto",
    "MOZILLA PUBLIC LICENSE": {
        "Version 1.0": "MPL-1.0"
    },
    "MakeIndex Distribution Notice": "MakeIndex",
    "Microsoft Public License (Ms-PL)": "MS-PL",
    "Microsoft Reciprocal License (Ms-RL)": "MS-RL",
    "MirOS License": "MirOS",
    "Mozilla Public License": {
        "Version 1.1": "MPL-1.1",
        "Version 2.0": "MPL-2.0"
    },
    "Multics License": "Multics",
    "NASA OPEN SOURCE AGREEMENT VERSION 1.3": "NASA-1.3",
    "NAUMEN Public License": "Naumen",
    "NETHACK GENERAL PUBLIC LICENSE": "NGPL",
    "NETIZEN OPEN SOURCE LICENSE": {
        "Version 1.0": "NOSL"
    },
    "NETSCAPE PUBLIC LICENSE Version 1.0": "NPL-1.0",
    "NO LIMIT PUBLIC LICENSE": "NLPL",
    "NRL License": "NRL",
    "NTP License (NTP)": "NTP",
    "Netscape Public LIcense version 1.1": "NPL-1.1",
    "Nokia Open Source License (NOKOS License)": "Nokia",
    "Non-Profit Open Software License 3.0": "NPOSL-3.0",
    "Norwegian Licence for Open Government Data (NLOD)": "NLOD-1.0",
    "Noweb is copyright 1989-2000 by Norman Ramsey. All rights reserved.": "Noweb",
    "OCLC Research Public License 2.0": "OCLC-2.0",
    "ODC Open Database License (ODbL)": "ODbL-1.0",
    "OPEN PUBLIC LICENSE": {
        "Version 1.0": "OPL-1.0"
    },
    "ORIGINAL LICENSE: This software is": "xinetd",
    "OSET Public License": "OSET-PL-2.1",
    "Open CASCADE Technology Public License": {
        "Version 6.6, April 2013": "OCCT-PL"
    },
    "Open Data Commons - Public Domain Dedication & License (PDDL)": "PDDL-1.0",
    "Open Software License v. 3.0 (OSL-3.0)": "OSL-3.0",
    "Open Software Licensev. 2.0": "OSL-2.0",
    "OpenSSL License": "OpenSSL",
    "PS Utilities Package": "psutils",
    "PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2": "Python-2.0",
    "Permission is granted to anyone to use this software for any purpose on any computer system, and to redistribute it freely, subject to the following restrictions:": {
        "The author is not responsible for the consequences of use of this software, no matter how awful, even if they arise from defects in it.": "Spencer-86",
        "This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.": "Newsletr"
    },
    "Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies.": "Latex2e",
    "Permission is hereby granted, free of charge, to any person obtaining a copy of this documentation file to use, copy, publish, distribute, sublicense, and/or sell copies of the documentation, and to permit others to do the same, provided that:": "Adobe-Glyph",
    r"Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files \(the \"+Software\"+\), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:": {
        "The above copyright notice and this permission notice shall be included in all copies of the Software and its Copyright notices. In addition publicly documented acknowledgment must be given that this software has been used if no source code of this software is made available publicly. This includes acknowledgments in either Copyright notices, Manuals, Publicity and Marketing documents or any documentation provided with any product containing this software. This License does not apply to any software that links to the libraries provided by this software (statically or dynamically), but only to the software provided.": "MIT-enna",
        "The above copyright notice and this permission notice shall be included in all copies of the Software and its documentation and acknowledgment shall be given in the documentation and software packages that this Software was used.": "MIT-feh",
        "The above copyright notice and this permission notice shall be included in all copies of the Software, its documentation and marketing & publicity materials, and acknowledgment shall be given in the documentation, materials and software packages that this Software was used.": "MIT-advertising",
        "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.": {
            "Distributions of all or part of the Software intended to be used by the recipients as they would use the unmodified Software, containing modifications that substantially alter, remove, or disable functionality of the Software, outside of the documented configuration mechanisms provided by the Software, shall be modified such that the Original Author's bug reporting email addresses and urls are either replaced with the contact information of the parties responsible for the changes, or removed entirely.": "MITNFA",
            "THE SOFTWARE IS PROVIDED .AS IS., WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.": "MIT",
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.": "MIT"
        }
    },
    "Permission to use, copy, and distribute this software and its documentation for any purpose with or without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation.": "gnuplot",
    "Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.": "0BSD",
    "Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that (i) the above copyright notices and this permission notice appear in all copies of the software and related documentation, and (ii) the names of Sam Leffler and Silicon Graphics may not be used in any advertising or publicity relating to the software without the specific, prior written permission of Sam Leffler and Silicon Graphics.": "libtiff",
    "Portions of this software were developed by the Unidata Program at the University Corporation for Atmospheric Research.": "NetCDF",
    "PostgreSQL Database Management System": "PostgreSQL",
    "Rdisc (this program) was developed by Sun Microsystems, Inc. and is provided for unrestricted use provided that this legend is included on all tape media and as a part of the software program in whole or part. Users may copy or modify Rdisc without charge, and they may freely distribute it.": "Rdisc",
    "RealNetworks Public Source License Version 1.0": "RPSL-1.0",
    "Reciprocal Public License 1.5 (RPL1.5)": "RPL-1.5",
    "Reciprocal Public License, version 1.1": "RPL-1.1",
    "Red Hat eCos Public License v1.1": "RHeCos-1.1",
    "Redistribution and use in any form of this material and any product thereof including software in source or binary forms, along with any related documentation, with or without modification (\"this material\"), is permitted provided that the following conditions are met:": "AMDPLPA",
    "Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:": {
        "Redistribution of source code must retain the above copyright notice, this list of conditions and the following disclaimer.": "BSD-3-Clause-No-Nuclear",
        "Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.": "Saxpath",
        "Redistributions of source code must retain the above copyright notice, this list of conditions and the following DISCLAIMER.": "Mup",
        "Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.": {
            "Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.": {
                "All advertising materials mentioning features or use of this software must display the following acknowledgement:": "BSD-4-Clause",
                "All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by the .*": "BSD-4-Clause",
                "All advertising materials mentioning features or use of this software must display the following acknowledgment: \"This product includes software developed by the .*.\"": "Apache-1.0",
                "Neither the name of .* nor the names of .* may be used to endorse or promote products derived from this software without specific prior written permission.": {
                    "THIS SOFTWARE IS PROVIDED.*": "BSD-3-Clause",
                    "Redistributions of any form whatsoever must retain the following acknowledgment: 'This product includes software developed by the .*": "BSD-3-Clause-Attribution",
                },
                "Redistributions in any form must be accompanied by information on how to obtain complete source code for the DB software and any accompanying software that uses the DB software. The source code must either be included in the distribution or be available for no more than the cost of distribution plus a nominal fee, and must be freely redistributable under reasonable conditions. For an executable file, complete source code means the source code for all modules it contains. It does not include source code for modules or files that typically accompany the major components of the operating system on which the executable file runs.": "Sleepycat",
                "Redistributions in any form must be accompanied by information on how to obtain complete source code for this software and any accompanying software that uses this software. The source code must either be included in the distribution or be available in a timely fashion for no more than the cost of distribution plus a nominal fee, and must be freely redistributable under reasonable and no more restrictive conditions. For an executable file, complete source code means the source code for all modules it contains. It does not include source code for modules or files that typically accompany the major components of the operating system on which the executable file runs.": "TOSL",
                "THIS SOFTWARE IS PROVIDED BY .* \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL .* BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES \\(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION\\) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT \\(INCLUDING NEGLIGENCE OR OTHERWISE\\) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.": "BSD-2-Clause",
            },
            "The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.": "bzip2-1.0.6"
        }
    },
    "Redistribution and use of this software and associated documentation (\"Software\"), with or without modification, are permitted provided that the following conditions are met:": "Plexus",
    "Redistribution and use of this software in source and binary forms, with or without modification, are permitted provided that the following conditions are met:": "BSD-Source-Code",
    "Ricoh Source Code Public License": {
        "Version 1.0": "RSCPL"
    },
    "SAX is free!": "SAX-PD",
    "SCEA Shared Source License 1.0": "SCEA",
    "SENDMAIL LICENSE": "Sendmail",
    "SGI FREE SOFTWARE LICENSE B": {
        "(Version 1.0 1/25/2000)": "SGI-B-1.0",
        "(Version 1.1 02/22/2000)": "SGI-B-1.1",
        "(Version 2.0, Sept. 18, 2008)": "SGI-B-2.0"
    },
    "SIL OPEN FONT LICENSE": {
        "Version 1.0 - 22 November 2005": "OFL-1.0",
        "Version 1.1 - 26 February 2007": "OFL-1.1"
    },
    "STANDARD ML OF NEW JERSEY COPYRIGHT NOTICE, LICENSE AND DISCLAIMER.": "SMLNJ",
    "STORAGE NETWORKING INDUSTRY ASSOCIATION": {
        "Version 1.1": "SNIA"
    },
    "SUGARCRM PUBLIC LICENSE": "SugarCRM-1.1.3",
    "SUN INDUSTRY STANDARDS SOURCE LICENSE": {
        "Version 1.2": "SISSL-1.2"
    },
    "SUN PUBLIC LICENSE Version 1.0": "SPL-1.0",
    "Secure Messaging Protocol (SMP) Libraries [ACL, CML, SFL]": "SMPPL",
    "Simple Public License (SimPL)": "SimPL-2.0",
    "Software License for MTL": "MTLL",
    "Sun Industry Standards Source License - Version 1.1": "SISSL",
    "Sybase Open Watcom Public License version 1.0": "Watcom-1.0",
    "THE FRAMEWORX OPEN LICENSE 1.0": "Frameworx-1.0",
    "THE Q PUBLIC LICENSE version 1.0": "QPL-1.0",
    "TORQUE v2.5+ Software License v1.1": "TORQUE-1.1",
    "The \"Artistic License\"": "Artistic-1.0-Perl",
    "The Academic Free License": {
        "v. 2.0": "AFL-2.0",
        "v.2.1": "AFL-2.1"
    },
    "The Artistic License": "Artistic-1.0",
    "The Artistic License 2.0": "Artistic-2.0",
    "The Clarified Artistic License": "ClArtistic",
    "The Clear BSD License": "BSD-3-Clause-Clear",
    "The Code Project Open License (CPOL) 1.02": "CPOL-1.02",
    "The Educational Community License": "ECL-1.0",
    "The FreeBSD Copyright": "BSD-2-Clause-FreeBSD",
    "The FreeType Project LICENSE": "FTL",
    "The LaTeX Project Public License": {
        "LPPL Version 1.1 1999-07-10": "LPPL-1.1",
        "LPPL Version 1.2 1999-09-03": "LPPL-1.2",
        "LPPL Version 1.3a 2004-10-01": "LPPL-1.3a",
        "LPPL Version 1.3c 2008-05-04": "LPPL-1.3c"
    },
    "The National Science and Technology Research Center for Computation and Visualization of Geometric Structures (The Geometry Center) University of Minnesota": "Qhull",
    "The Net Boolean Public License": "NBPL-1.0",
    "The Open Group Test Suite License": "OGTSL",
    "The Open Software License": {
        "v. 1.0": "OSL-1.0",
        "v. 1.1": "OSL-1.1",
        "v. 2.1": "OSL-2.1"
    },
    "The OpenLDAP Public License": {
        "Version 1.1, 25 August 1998": "OLDAP-1.1",
        "Version 1.2, 1 September 1998": "OLDAP-1.2",
        "Version 1.3, 17 January 1999": "OLDAP-1.3",
        "Version 1.4, 18 January 1999": "OLDAP-1.4",
        "Version 2.0, 7 June 1999": "OLDAP-2.0",
        "Version 2.0.1, 21 December 1999": "OLDAP-2.0.1",
        "Version 2.1, 29 February 2000": "OLDAP-2.1",
        "Version 2.2, 1 March 2000": "OLDAP-2.2",
        "Version 2.2.1, 1 March 2000": "OLDAP-2.2.1",
        "Version 2.2.2, 28 July 2000": "OLDAP-2.2.2",
        "Version 2.3, 28 July 2000": "OLDAP-2.3",
        "Version 2.4, 8 December 2000": "OLDAP-2.4",
        "Version 2.5, 11 May 2001": "OLDAP-2.5",
        "Version 2.6, 14 June 2001": "OLDAP-2.6",
        "Version 2.7, 7 September 2001": "OLDAP-2.7",
        "Version 2.8, 17 August 2003": "OLDAP-2.8"
    },
    "The PHP License,": {
        "version 3.0": "PHP-3.0",
        "version 3.01": "PHP-3.01"
    },
    "The SFL License Agreement": "iMatix",
    "The TMate Open Source License.": "TMate",
    "The Universal Permissive License (UPL), Version 1.0": "UPL-1.0",
    "The X.Net, Inc. License": "Xnet",
    "The Zend Engine License, version 2.00": "Zend-2.0",
    "The authors hereby grant permission to use, copy, modify, distribute, and license this software and its documentation for any purpose, provided that existing copyright notices are retained in all copies and that this notice is included verbatim in any distributions. No written agreement, license, or royalty fee is required for any of the authorized uses. Modifications to this software may be copyrighted by their authors and need not follow the licensing terms described here, provided that the new terms are clearly indicated on the first page of each file where they apply.": "SWL",
    "The BSD-2 license": "BSD-2-Clause",
    "The eCos license version 2.0": "deprecated_eCos-2.0",
    "The source code in this package is copyright 1999-2010 by Andrew Plotkin.": "Glulxe",
    "This FastCGI application library source and object code (the \"Software\") and its documentation (the \"Documentation\") are copyrighted by Open Market, Inc (\"Open Market\"). The following terms apply to all files associated with the Software and Documentation unless explicitly disclaimed in individual files.": "OML",
    "This code is derived from software contributed to The NetBSD Foundation by .*": "BSD-2-Clause-NetBSD",
    "This configure script is free software; the Free Software Foundation gives unlimited permission to copy, distribute and modify it.": "FSFUL",
    "This copy of the libpng notices is provided for your convenience. In case of any discrepancy between this copy and the notices in the file png.h that is included in the libpng distribution, the latter shall prevail.": "Libpng",
    "This file and the 14 PostScript(R) AFM files it accompanies may be used, copied, and distributed for any purpose and without charge, with or without modification, provided that all copyright notices are retained; that the AFM files are not distributed without this file; that all modifications to this file or any of the AFM files are prominently noted in the modified file(s); and that this paragraph is not modified. Adobe Systems has no responsibility or obligation to support the use of the AFM files.": "APAFML",
    "This file is free software; the Free Software Foundation gives unlimited permission to copy and/or distribute it, with or without modifications, as long as this notice is preserved.": "FSFULLR",
    "This file may be freely copied and redistributed as long as:": "Afmparse",
    "This file may be freely transmitted and reproduced, but it may not be changed unless the name is changed also (except that you may freely change the paper-size option for \\documentclass).": "Dotseqn",
    "This file was added by Clea F. Rees on 2008/11/30 with the permission of Dean Guenther and pointers to this file were added to all source files.": "Wsuipa",
    "This is APREAMBL.TEX, version 1.10e, written by Hans-Hermann Bode (HHBODE@DOSUNI1.BITNET), for the BibTeX `adaptable' family, version 1.10. See the file APREAMBL.DOC for a detailed documentation.": "Abstyles",
    "This is a package of commutative diagram macros built on top of Xy-pic by Michael Barr (email: barr@barrs.org). Its use is unrestricted. It may be freely distributed, unchanged, for non-commercial or commercial use. If changed, it must be renamed. Inclusion in a commercial software package is also permitted, but I would appreciate receiving a free copy for my personal examination and use. There are no guarantees that this package is good for anything. I have tested it with LaTeX 2e, LaTeX 2.09 and Plain TeX. Although I know of no reason it will not work with AMSTeX, I have not tested it.": "Barr",
    "This is free and unencumbered software released into the public domain.": "Unlicense",
    "This material was originally written and compiled by Wietse Venema at Eindhoven University of Technology, The Netherlands, in 1990, 1991, 1992, 1993, 1994 and 1995.": "TCP-wrappers",
    "This program is free software; you can redistribute it freely. Use it at your own risk; there is NO WARRANTY.": "XSkat",
    "This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.": "GPL-1.0",
    "This software is copyrighted by .* and other parties. The following terms apply to all files associated with the software unless explicitly disclaimed in individual files.": "TCL",
    "This software is distributed in the hope that it will be useful, but with NO WARRANTY OF ANY KIND.": "Leptonica",
    "This software is not subject to any license of the American Telephone and Telegraph Company or of the Regents of the University of California.": "Spencer-94",
    "This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.": {
        "Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:":
        {
            "The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment (see the following) in the product documentation is required.":
            {
                "Portions Copyright \u00a9 2002-2004 James W. Newkirk, Michael C. Two, Alexei A. Vorontsov, Charlie Poole or Copyright \u00a9 2000-2004 Philip A. Craig": "Nunit",
                "Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.": "zlib-acknowledgement"
            }
        }
    },
    "This source code has been made available to you by IBM on an AS-IS basis. Anyone receiving this source is licensed under IBM copyrights to use it in any way he or she deems fit, including copying it, modifying it, compiling it, and redistributing it either with or without modifications. No license under IBM patents or patent applications is to be implied by the copyright license.": "IBM-pibs",
    "This work is being provided by the copyright holders under the following license.": "W3C-20150513",
    "UNICODE, INC. LICENSE AGREEMENT - DATA FILES AND SOFTWARE": {
        "Unicode Data Files include all data files under the directories http://www.unicode.org/Public/, http://www.unicode.org/reports/, and http://www.unicode.org/cldr/data/. Unicode Data Files do not include PDF online code charts under the directory http://www.unicode.org/Public/. Software includes any source code published in the Unicode Standard or under the directories http://www.unicode.org/Public/, http://www.unicode.org/reports/, and http://www.unicode.org/cldr/data/.": "Unicode-DFS-2015",
        "Unicode Data Files include all data files under the directories http://www.unicode.org/Public/, http://www.unicode.org/reports/, http://www.unicode.org/cldr/data/, http://source.icu-project.org/repos/icu/, and http://www.unicode.org/utility/trac/browser/.": "Unicode-DFS-2016"
    },
    "Unicode Terms of Use": "Unicode-TOU",
    "University of Illinois/NCSA Open Source License": "NCSA",
    "Use and copying of this software and preparation of derivative works based upon this software are permitted. Any copy of this software or of any derivative work must include the above copyright notice of Xerox Corporation, this paragraph and the one after it. Any distribution of this software or derivative works must comply with all applicable United States export control laws.": "Xerox",
    "Use is subject to license terms.": "BSD-3-Clause-No-Nuclear-License-2014",
    "VIM LICENSE": "Vim",
    "VOSTROM Public License for Open Source": "VOSTROM",
    "Version 1.0.5 of 10 December 2007": "bzip2-1.0.5",
    "Vovida Software License v. 1.0": "VSL-1.0",
    "W3C SOFTWARE NOTICE AND LICENSE": "W3C",
    "W3C\u00ae SOFTWARE NOTICE AND LICENSE": "W3C-19980720",
    "X11 License": "X11",
    "XFree86 License (version 1.1)": "XFree86-1.1",
    "Yahoo! Public License, Version 1.0 (YPL)": "YPL-1.0",
    "Yahoo! Public License, Version 1.1 (YPL)": "YPL-1.1",
    "You can use DOC software in commercial and/or binary software releases and are under no obligation to redistribute any of your source code that is built using DOC software. Note, however, that you may not misappropriate the DOC software code, such as copyrighting it yourself or claiming authorship of the DOC software code, in a way that will prevent DOC software from being distributed freely using an open-source development model. You needn't inform anyone that you're using DOC software in your software, though we encourage you to let us know so we can promote your project in the DOC software success stories.": "DOC",
    "You may copy and distribute this file freely. Any queries and complaints should be forwarded to Jim.Davies@comlab.ox.ac.uk.": "Zed",
    "You may freely use, modify, and/or distribute each of the files in this package without limitation. The package consists of the following files:": "Borceux",
    "Zimbra Public License, Version 1.3 (ZPL)": "Zimbra-1.3",
    "Zimbra Public License, Version 1.4 (ZPL)": "Zimbra-1.4",
    "Zope Public License (ZPL) Version 1.1": "ZPL-1.1",
    "Zope Public License (ZPL) Version 2.0": "ZPL-2.0",
    "Zope Public License (ZPL) Version 2.1": "ZPL-2.1",
    "cwpuzzle.dtx is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. No author or distributor accepts responsibility to anyone for the consequences of using it or for whether it serves any particular purpose or works at all, unless he says so in writing.": "Crossword",
    "gSOAP Public License": "gSOAP-1.3b",
    "insert GPL v2 text here": "deprecated_GPL-2.0-with-GCC-exception",
    "insert GPL v3 text here": "deprecated_GPL-3.0-with-autoconf-exception",
    "psfrag.dtx": "psfrag",
    "wxWindows Library Licence, Version 3.1": "deprecated_WXwindows",
    "zlib License": "Zlib",
    "\ufeffinsert GPL v2 license text here": {
        "Autoconf Exception": "deprecated_GPL-2.0-with-autoconf-exception",
        "Class Path Exception": "deprecated_GPL-2.0-with-classpath-exception"
    },
    "\ufeffinsert GPL v2 text here": "deprecated_GPL-2.0-with-font-exception",
    "\ufeffinsert GPL v3 text here": "deprecated_GPL-3.0-with-GCC-exception",
    "Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at": "Apache-2.0",
    "Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION": "Apache-2.0",
    "Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.": "ISC"
}
