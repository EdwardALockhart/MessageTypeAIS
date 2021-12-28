"""
Copyright (C) Edward Alan Lockhart 2021

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see https://www.gnu.org/licenses/.
"""

def message_type_ais(message):
    types = {1: "Position Report Class A",
             2: "Position Report Class A (Assigned schedule)",
             3: "Position Report Class A (Response to interrogation)",
             4: "Base Station Report",
             5: "Static and Voyage Related Data",
             6: "Binary Addressed Message",
             7: "Binary Acknowledge",
             8: "Binary Broadcast Message",
             9: "Standard SAR Aircraft Position Report",
             10: "UTC and Date Inquiry",
             11: "UTC and Date Response",
             12: "Addressed Safety Related Message",
             13: "Safety Related Acknowledgement",
             14: "Safety Related Broadcast Message",
             15: "Interrogation",
             16: "Assignment Mode Command",
             17: "DGNSS Binary Broadcast Message",
             18: "Standard Class B CS Position Report",
             19: "Extended Class B Equipment Position Report",
             20: "Data Link Management",
             21: "Aid-to-Navigation Report",
             22: "Channel Management",
             23: "Group Assignment Command",
             24: "Static Data Report",
             25: "Single Slot Binary Message",
             26: "Multiple Slot Binary Message With Communications State",
             27: "Position Report For Long-Range Applications"}
    
    i = ord(message.split(',')[5][0])
    i -= 48
    if i > 40:
        i -= 8
    if i not in types.keys():
        return None
    else:
        return types[int("{0:b}".format(i).zfill(6), 2)]

message = "!AIVDM,1,1,,A,18UG;P0012G?Uq4EdHa=c;7@051@,0*53"
message_type = message_type_ais(message)
