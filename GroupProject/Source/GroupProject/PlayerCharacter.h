// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "PlayerCharacter.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE(FPlayerDelegate);

class AHumanPlayerController;

UCLASS()
class GROUPPROJECT_API APlayerCharacter : public ACharacter
{
	GENERATED_BODY()

		UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class USpringArmComponent* SpringArm;

		UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class UCameraComponent* Camera;

		

public:

	FPlayerDelegate OnDeath;

	// Sets default values for this character's properties
	APlayerCharacter();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser) override;


	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* InputComponent) override;

	/** Base turn rate, in deg/sec. Other scaling may affect final turn rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseTurnRate;

	/** Base look up/down rate, in deg/sec. Other scaling may affect final rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseLookUpRate;

	AHumanPlayerController* GetHumanController();

	/** Called for forwards/backward input */
	void MoveForward(float Value);

	/** Called for side to side input */
	void MoveRight(float Value);

	void TurnAtRate(float Rate);

	void LookUpRate(float Rate);

	void OnFire();

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
	int GetCurrentHealth() const;

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
	int GetCurrentArmor() const;

protected:
	void CameraZoomIn();

	void CameraZoomOut();


	UPROPERTY(VisibleAnywhere, Category = "Camera")
	float CameraZoom;
	
	//The length of which that subtracts and adds to the target arm and lengths 
	UPROPERTY(EditDefaultsOnly, Category = "Camera")
	float CameraZoomLength = 250;

private:

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
	int32 CurrentHealth;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumArmor = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
		int32 CurrentArmor;


};
