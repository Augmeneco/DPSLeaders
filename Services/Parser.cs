using Newtonsoft.Json.Linq;
using System.IO;
using System.Text.Json.Nodes;

public class Parser
{
    int limit = 100;
    int offset = 0;
    string main_api_url = "https://simpact.app/api/db";
    JObject leaderboard = new JObject();
    bool end_of_list = false;

    public void ParseData()
    {
        while(!end_of_list){
            Console.WriteLine("Parsing offset = "+offset);
            /*    params = {
    'q': json.dumps({"query":{},"limit":limit,"skip":offset}),
    }
    response = requests.get(main_api_url, params=params).json()
    if 'data' not in response: break
    teams = response['data']*/

            
        }
    }
}