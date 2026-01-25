local HttpService = game:GetService("HttpService")
local ServerStorage = game:GetService("ServerStorage")

local targetFolders = {
    ["UnitData"] = workspace:FindFirstChild("UnitData"),
    ["ItemData"] = workspace:FindFirstChild("ItemData"),
    ["EvolutionsData"] = workspace:FindFirstChild("EvolutionsData"),
    ["MapData"] = workspace:FindFirstChild("MapData"),
    ["EvoData"] = workspace:FindFirstChild("EvoData"),
    ["DropData"] = workspace:FindFirstChild("DropData")
}

local MAX_CHARS = 180000 

local mainExportFolder = ServerStorage:FindFirstChild("Bulk_Exports") or Instance.new("Folder")
mainExportFolder.Name = "Bulk_Exports"
mainExportFolder.Parent = ServerStorage

local function saveChunk(parent, name, dataTable)
    local export = Instance.new("ModuleScript")
    export.Name = name
    export.Source = "return [=[" .. HttpService:JSONEncode(dataTable) .. "]=]"
    export.Parent = parent
end

local function exportFlattened(instance, parentExportFolder)
    local currentChunk = {}
    local currentSize = 0
    local partCount = 1
    
    local descendants = instance:GetDescendants()
    for _, obj in ipairs(descendants) do
        if obj:IsA("ModuleScript") then
            local src = obj.Source
            if #src > 0 and not src:find("pairs(script:GetChildren())") then
                if (currentSize + #src) > MAX_CHARS and next(currentChunk) then
                    saveChunk(parentExportFolder, "DATA_PART_" .. partCount, currentChunk)
                    currentChunk = {}
                    currentSize = 0
                    partCount += 1
                end

                local key = obj.Name
                if currentChunk[key] then
                    key = obj.Parent.Name .. "_" .. obj.Name
                end

                currentChunk[key] = src
                currentSize = currentSize + #src
            end
        end
    end

    if next(currentChunk) then
        local name = (partCount == 1) and "DATA_CONTENTS" or ("DATA_PART_" .. partCount)
        saveChunk(parentExportFolder, name, currentChunk)
    end
end

mainExportFolder:ClearAllChildren()

for name, instance in pairs(targetFolders) do
    if instance then
        print("Processing Category: " .. name)
        local categoryRoot = Instance.new("Folder")
        categoryRoot.Name = name .. "_Export"
        categoryRoot.Parent = mainExportFolder
        
        if name == "DropData" then
            for _, subCategory in ipairs(instance:GetChildren()) do
                local subFolder = Instance.new("Folder")
                subFolder.Name = subCategory.Name
                subFolder.Parent = categoryRoot
                
                print("  Flattening: " .. subCategory.Name)
                exportFlattened(subCategory, subFolder)
            end
        else
            exportFlattened(instance, categoryRoot)
        end
    end
end

print("-----------------------------------------")
print("All DropData flattened successfully!")