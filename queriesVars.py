
def test():
    return "Test"

def getQueries(varname,daysgo, prod, events = ""):


    query = f"""
            SELECT a.date,
                u.login
                ,u.name
                ,ti.name 
                ,ev.name 
                -- ,a.tool
                -- ,u.id 
                -- ,a.event
                ,a.search
                ,a.key1
                ,a.key2
                ,a.quantity
                ,tick.t_key 
                ,tick.summary 
            FROM ops_knowledge._users u
            JOIN ops_knowledge._analytics a ON u.id = a.user_id
            JOIN ops_knowledge.`_tools_info_event` ev on a.event = ev.id
            JOIN ops_knowledge.`_tools_info` ti on a.tool = ti.id 
            LEFT JOIN ops_knowledge.`_tickets` tick on a.ops_ticket = tick.id 
            WHERE  	 

                    a.date >= DATE(CURRENT_DATE - INTERVAL {daysgo} DAY)
                    AND prod in ({prod})            
                    {events}
            LIMIT 10
            ORDER BY u.name ASC
        """
    
    # print(query)
    # return query
    
    queryEventsAgg = f"""
            SELECT  a.date               
                    ,ti.name 
                    ,COUNT(ti.name) as 'count'
            FROM ops_knowledge._analytics a
            JOIN ops_knowledge.`_tools_info` ti on a.tool = ti.id
            WHERE   a.date >= DATE(CURRENT_DATE - INTERVAL {daysgo} DAY)
                    AND prod in ({prod})            
                    {events}
            GROUP BY a.date,ti.name
            ORDER BY date DESC, name ASC
        """
    
    if (varname == "main"):
        return query
    elif(varname == "toolname"):
        return queryEventsAgg
    
    