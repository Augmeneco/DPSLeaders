using Newtonsoft.Json.Linq;
using System.IO;
using System.Threading.Tasks;
using Microsoft.Extensions.Caching.Memory;

public interface IDataService
{
    JObject GetDbData(bool reload=false);
    JObject GetInfoData(bool reload=false);

}

public class DataService : IDataService
{
    private JObject _cachedDb;
    private JObject _cachedData;

    public JObject GetDbData(bool reload=false)
    {
        if (_cachedDb == null || reload)
        {
            var json = File.ReadAllText("wwwroot/data/db.json");
            _cachedDb = JObject.Parse(json);
        }

        return _cachedDb;
    }
    public JObject GetInfoData(bool reload=false)
    {
        if (_cachedData == null || reload)
        {
            var json = File.ReadAllText("wwwroot/data/info.json");
            _cachedData = JObject.Parse(json);
        }

        return _cachedData;
    }
}
