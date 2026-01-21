local HttpService = game:GetService("HttpService")
local ServerStorage = game:GetService("ServerStorage")

local targetFolders = {
    ["UnitData"] = workspace:FindFirstChild("UnitData"),
    ["ItemData"] = workspace:FindFirstChild("ItemData"),
    ["EvolutionsData"] = workspace:FindFirstChild("EvolutionsData"),
    ["MapData"] = workspace:FindFirstChild("MapData")
}

local mainExportFolder = ServerStorage:FindFirstChild("Bulk_Exports") or Instance.new("Folder")
mainExportFolder.Name = "Bulk_Exports"
mainExportFolder.Parent = ServerStorage

local function exportFolder(folderName, folderInstance)
    if not folderInstance then 
        warn("Folder not found: " .. folderName)
        return 
    end

    print("Starting deep export for: " .. folderName)
    
    local categoryFolder = Instance.new("Folder")
    categoryFolder.Name = folderName .. "_Export"
    categoryFolder.Parent = mainExportFolder

    local allItems = folderInstance:GetDescendants()
    local currentBulk = {}
    local currentSize = 0
    local fileCount = 1

    local modulesToExport = {}
    for _, obj in ipairs(allItems) do
        if obj:IsA("ModuleScript") and obj ~= folderInstance then
            if #obj.Source > 0 then
                table.insert(modulesToExport, obj)
            end
        end
    end

    for i, module in ipairs(modulesToExport) do
        local src = module.Source
        currentBulk[module.Name] = src
        currentSize += #src
        
        if currentSize > 150000 or i == #modulesToExport then
            local export = Instance.new("ModuleScript")
            export.Name = "PART_" .. fileCount
            export.Source = "return [=[" .. HttpService:JSONEncode(currentBulk) .. "]=]"
            export.Parent = categoryFolder
            
            print("  - Saved Part " .. fileCount .. " (" .. currentSize .. " chars)")
            
            fileCount += 1
            currentBulk = {}
            currentSize = 0
        end
    end
end

for name, instance in pairs(targetFolders) do
    exportFolder(name, instance)
end

print("-----------------------------------------")
print("Deep Export Done!")