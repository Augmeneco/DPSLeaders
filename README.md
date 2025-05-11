# 🎮 DPS Leaders - Genshin Impact Team Optimizer ⚔️

✨ ASP.NET Blazor application for analyzing and optimizing Genshin Impact team compositions with focus on DPS performance and character synergy. ✨

🌐 **Live demo:** [https://dpsleaders.augmeneco.ru](https://dpsleaders.augmeneco.ru)

## 🔑 Key Features

- 📊 Display of team DPS with character descriptions
- 🎯 Average crit rate/damage calculation based on user input
- ⚖️ Configuration file balancing for gcsim calculator
- 🔐 Admin interface for managing character data

## 🏆 Advantages over [simpact.app](https://simpact.app/)

Our solution provides better F2P character team balancing by:
- 🛡️ Accounting for realistic artifact quality for F2P players
- ⚡ Optimizing for character constellations commonly available to F2P

## 🛠️ Build Instructions

1. 📥 Install .NET 9 SDK
2. 🖇️ Clone this repository
3. 🔄 Restore dependencies:
```bash
dotnet restore
```

### 🧑‍💻 Development
For development with hot reload:
```bash
dotnet watch
```

### 🚀 Production Build
1. 🔨 Build Release version:
```bash
dotnet build -c Release
```
2. 📦 Publish self-contained executable:
```bash
dotnet publish -c Release -o ./dpsleaders --self-contained true /p:PublishSingleFile=true
```

🌐 The application will be available at `http://localhost:5001` by default in development mode.
