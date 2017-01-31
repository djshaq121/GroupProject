// Copyright 

#pragma once

#include "GameFramework/Actor.h"
#include "test.generated.h"

UCLASS()
class GROUPPROJECT_API Atest : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	Atest();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	
	
};
