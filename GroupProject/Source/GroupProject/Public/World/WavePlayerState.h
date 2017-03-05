// Copyright LostGods

#pragma once

#include "GameFramework/PlayerState.h"
#include "WavePlayerState.generated.h"

/**
 * 
 */
UCLASS()
class GROUPPROJECT_API AWavePlayerState : public APlayerState
{
	GENERATED_BODY()
	
	
public:
	void AddGold(int32 Amount);

	UFUNCTION(BlueprintCallable, Category = "Score")
	int32 GetGold() const;

private:
	UPROPERTY()
	int32 Gold;

	
};
